from pdfminer.high_level import extract_text
import variables
from itertools import islice
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

    lines = text.split("\n")  # split text into lines
    paragraphs = text.split("\n\n")  # split text into paragraphs

    max_line_length = max([len(line) for line in lines if len(line) < 80])  # get max line length
    paragraph_length = max_line_length * 4  # define paragraph length

    # clean paragraphs to avoid non-informational characters
    cleaned_paragraphs = [re.sub(r'[^a-zA-Z0-9$€ !?.]', '', paragraph) for paragraph in paragraphs]
    cleaned_paragraphs = [paragraph.strip(' \n') for paragraph in cleaned_paragraphs]
    print(cleaned_paragraphs)

    filtered_text = [paragraph for paragraph in cleaned_paragraphs if len(paragraph) > paragraph_length]  # filter lines
    print(filtered_text)

    return filtered_text


def batch(filtered_text: list, batch_size: int):
    """
    Function to batch the text
    :param filtered_text: Text that has been filtered by text_cleaner()
    :param batch_size: Amount of tokens of each request
    """

    batched_text = []

    text = " ".join(filtered_text)

    enc = tiktoken.encoding_for_model(variables.variable["model"])
    tokenized_element = enc.encode(text)

    it = iter(tokenized_element)
    while batch := tuple(islice(it, batch_size)):
        batched_text.append(batch)

    return batched_text

text_cleaner("/Users/sping/Downloads/_10-Q-Q2-2023-As-Filed.pdf")