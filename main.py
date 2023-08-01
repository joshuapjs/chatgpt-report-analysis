import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

# an example question about the 2022 Olympics
query = input("How can I help you ?\n:")

response = openai.ChatCompletion.create(
    messages=[
        {'role': 'system', 'content': 'You answer questions about the 2022 Winter Olympics.'},
        {'role': 'user', 'content': query},
    ],
    model=GPT_MODEL,
    temperature=0,
)

print(response['choices'][0]['message']['content'])
