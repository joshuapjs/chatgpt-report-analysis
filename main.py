import prepare_pdf as prep
import variables
import time
import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')


def get_response(file_path: str):
    content = prep.batch(prep.text_cleaner(file_path), variables.variable["request_size"])
    every_response = []
    token_count = 0

    # text of the financial report
    for prompt in content:
        response = openai.Completion.create(
            model=variables.variable["model"],
            prompt=prompt,
            max_tokens=1,
            temperature=0,
        )
        time.sleep(1)
        every_response.append(response)
        time.sleep(1)

    # last response
    last_prompt = openai.Completion.create(
        model=variables.variable["model"],
        prompt="Finished. What does the report tell about the short term growth prospect of the company?"
               "And ist it financially stable?",
        max_tokens=4057,
        temperature=0,
    )

    every_response.append(last_prompt)

    return every_response[-1]["choices"][0]["text"]
