import prepare_pdf as prep
import variables
import tiktoken
import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')


def get_response(file_path: str):
    enc = tiktoken.encoding_for_model(variables.variable["model"])
    messages = prep.batch(prep.text_cleaner(file_path), (variables.variable["request_size"]
                                                         - variables.variable["answer_size"]
                                                         - len(enc.encode(variables.variable["question"]))))

    print(messages)
    response = openai.ChatCompletion.create(
        model=variables.variable["model"],
        messages=messages,
        max_tokens=variables.variable["answer_size"],
        temperature=0,
    )

    return response["choices"][0]["message"]


print(get_response("/Users/sping/Downloads/AEL 04-07-22_F.pdf"))
