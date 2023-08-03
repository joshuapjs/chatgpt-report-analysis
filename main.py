from prepare_pdf import textcleaner
import openai
import time
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

def get_response(file_path: str):

    content = textcleaner(file_path)
    every_response = []

    # first response
    first_prompt = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt="You will know receive a lot of text. Please wait."
               " I indicate when I am finished.",
        max_tokens=7,
        temperature=0,
    )
    every_response.append(first_prompt)

    # text of the financial report
    for prompt in content:
        response = openai.Completion.create(
              model="gpt-3.5-turbo",
              prompt=prompt,
              max_tokens=2000,
              temperature=0,
            )
        every_response.append(response)

    # last response
    last_prompt = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt="Okay I am finished. please give me an overview about the current situation"
               " and the most important facts.",
        max_tokens=2000,
        temperature=0,
    )
    every_response.append(last_prompt)

    return every_response
