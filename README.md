# Q4: Structured Output

This repository contains the solution for Question 4 of the assignment.

## Description

A Python script that generates tweets using a prompt template and the Google Gemini LLM. The LLM is instructed to return a JSON object with keys: `tweet`, `word_count`, and `sentiment`. The output is validated using Pydantic, and an error is raised if validation fails.

## Usage

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/HarshRajj/intern-2025-q4.git
    cd intern-2025-q4
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Create a `.env` file** and add your Google API key:
    ```
    GOOGLE_API_KEY="YOUR_API_KEY_HERE"
    ```

4.  **Run the script:**
    ```bash
    python main.py
    ```

## Demo 

[Run Google Colab Notebook](https://colab.research.google.com/drive/1N8XuYgMx-cQlfHGhoVgFh2vjpXYEBxfy?usp=sharing)
