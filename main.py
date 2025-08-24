import os
import json
from google import generativeai as genai
from dotenv import load_dotenv
from pydantic import BaseModel, ValidationError

GEMINI_MODEL = 'gemini-2.0-flash'

class TweetResponse(BaseModel):
    tweet: str
    word_count: int
    sentiment: str

TWEET_SAMPLES = [
    {"topic": "the future of renewable energy", "tone": "optimistic", "max_words": 30},
    {"topic": "tips for effective remote work", "tone": "professional", "max_words": 25},
    {"topic": "the joy of discovering new music", "tone": "enthusiastic", "max_words": 35},
]

def generate_tweet(topic: str, tone: str, max_words: int) -> None:
    prompt = (
        f"Generate a tweet as a JSON object with the following keys: 'tweet', 'word_count', and 'sentiment'. "
        f"The tweet should be about '{topic}', have a {tone} tone, and be under {max_words} words. "
        f"Example format: {{\"tweet\": \"...\", \"word_count\": 23, \"sentiment\": \"positive or negative\"}}. "
        f"Do not include hashtags or URLs. Only output the JSON."
    )
    model = genai.GenerativeModel(GEMINI_MODEL)
    response = model.generate_content(prompt)
    raw = response.text.strip()
    # Remove markdown code block markers if present
    if raw.startswith('```'):
        raw = raw.lstrip('`')
        # Remove the language hint if present (e.g., json) and any leading/trailing whitespace
        raw = raw.split('\n', 1)[-1].rsplit('```', 1)[0].strip()
    try:
        data = json.loads(raw)
        validated = TweetResponse(**data)
        print("--- Validated Tweet JSON ---")
        print(json.dumps(validated.model_dump(), indent=2))
        print("-" * 20 + "\n")
    except (json.JSONDecodeError, ValidationError) as e:
        raise RuntimeError(f"Validation failed for topic '{topic}': {e}\nRaw response: {response.text}\n")

def main() -> None:
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("Error: GOOGLE_API_KEY was not found. Please check your .env file.")
        return
    genai.configure(api_key=api_key)
    for sample in TWEET_SAMPLES:
        generate_tweet(
            topic=sample["topic"],
            tone=sample["tone"],
            max_words=sample["max_words"]
        )

if __name__ == "__main__":
    main()
