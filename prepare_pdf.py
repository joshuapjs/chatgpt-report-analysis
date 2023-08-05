from pdfminer.high_level import extract_text
import variables
import tiktoken
import re


def text_cleaner(pdf_file: str):
    """
    Function to select only lines that are lo
    ng enough
    From which I expect that they are pure text lines and therefore
    relevant for and interpretable by ChatGPT
    :param pdf_file: path to pdf file
    """
    text = extract_text(pdf_file)  # extract text from pdf
    enc = tiktoken.encoding_for_model(variables.variable["model"])
    number_of_tokens = variables.variable["request_size"]
    lines_per_paragraph = 2
    filtered_text = []

    lines = text.split("\n")  # split text into lines
    paragraphs = text.split("\n\n")  # split text into paragraphs

    max_line_length = max([len(line) for line in lines if len(line) < 80])  # get max line length

    while number_of_tokens > (variables.variable["request_size"]
                              - variables.variable["answer_size"]
                              - len(enc.encode(variables.variable["question"]))):

        paragraph_length = max_line_length * lines_per_paragraph  # define paragraph length

        # clean paragraphs to avoid non-informational characters
        cleaned_paragraphs = [re.sub(r'[^a-zA-Z0-9$€ !?.]', '', paragraph) for paragraph in paragraphs]
        cleaned_paragraphs = [paragraph.strip(' \n') for paragraph in cleaned_paragraphs]

        filtered_text = [paragraph for paragraph in cleaned_paragraphs if len(paragraph) > paragraph_length]

        text = " ".join(filtered_text)
        tokenized_text = enc.encode(text)
        number_of_tokens = len(tokenized_text)

        lines_per_paragraph += 1

    return filtered_text


def batch(filtered_text: list, batch_size: int):
    """
    :param filtered_text: Text that has been filtered by text_cleaner()
    :param batch_size: Amount of tokens of each request
    """

    messages = []

    for message in filtered_text:
        messages.append({"role": "user", "content": message})
    messages.append({"role": "user", "content": variables.variable["question"]})

    return messages
