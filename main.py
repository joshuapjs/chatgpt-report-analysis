import prepare_pdf as prep
import variables
import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')


def get_response(file_path: str):

    # Prepare the text for the API call
    messages = prep.format_to_messages(prep.text_cleaner(file_path))

    # OpenAI API call
    response = openai.ChatCompletion.create(
        model=variables.variable["model"],
        messages=messages,
        max_tokens=variables.variable["answer_size"],
        temperature=0,
    )

    return response["choices"][0]["message"]["content"]
