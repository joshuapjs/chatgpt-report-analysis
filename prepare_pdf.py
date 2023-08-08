from pdfminer.high_level import extract_text
from . import variables
import tiktoken
import re


def text_cleaner(pdf_file: str):
    """
    Function to select only paragraphs that are long enough
    The selection is based on the assumption that the longer the paragraph the more information it contains
    :param pdf_file: path to pdf file
    """
    text = extract_text(pdf_file)
    enc = tiktoken.encoding_for_model(variables.variable["model"])  # get the encoding of the model
    number_of_tokens = variables.variable["request_size"]
    lines_per_paragraph = 2
    selected_paragraphs = []

    # Splitting the text into subsections
    lines = text.split("\n")
    paragraphs = text.split("\n\n")

    max_line_length = max([len(line) for line in lines if len(line) < 80])

    # Adjusting the paragraph selection to the request size
    # If the request becomes too big the paragraphs increase in size, one line per iteration
    while number_of_tokens > (variables.variable["request_size"]
                              - variables.variable["answer_size"]
                              - len(enc.encode(variables.variable["question"]))):

        paragraph_length = max_line_length * lines_per_paragraph

        # Clean paragraphs to avoid non-informational characters
        cleaned_paragraphs = [re.sub(r'[^a-zA-Z0-9$€ !?.]', '', paragraph) for paragraph in paragraphs]
        cleaned_paragraphs = [paragraph.strip(' \n') for paragraph in cleaned_paragraphs]

        selected_paragraphs = [paragraph for paragraph in cleaned_paragraphs if len(paragraph) >= paragraph_length]

        text = " ".join(selected_paragraphs)
        tokenized_text = enc.encode(text)
        number_of_tokens = len(tokenized_text)

        lines_per_paragraph += 1

    return selected_paragraphs


def format_to_messages(filtered_text: list):
    """
    :param filtered_text: Selected paragraphs from the text_cleaner function
    """

    messages = []

    for paragraph in filtered_text:
        messages.append({"role": "user", "content": paragraph})
    messages.append({"role": "user", "content": variables.variable["question"]})

    return messages
