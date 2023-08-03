import prepare_pdf as prep
from variables import model
import time
import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')


def get_response(file_path: str):

    content = prep.batch(prep.text_cleaner(file_path), 1000)
    every_response = []
    token_count = 0

    # text of the financial report
    for prompt in content:
        token_count =+ len(prompt) + 1
        response = openai.Completion.create(
            model=model,
            prompt=prompt,
            max_tokens=1,
            temperature=0,
            )
        time.sleep(1)
        if token_count >= 4050:
            time.sleep(60)
        every_response.append(response)
        time.sleep(1)

    # last response
    last_prompt = openai.Completion.create(
        model=model,
        prompt="Okay I am finished. please give me an overview about the current situation of the company"
               " and the most important facts.",
        max_tokens=3000,
        temperature=0,
    )
    
    every_response.append(last_prompt)

    return every_response[-1]["choices"][0]["text"]
