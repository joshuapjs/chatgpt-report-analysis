from pdfminer.high_level import extract_text
import re


def textcleaner(pdf_file: str):
    """
    Function to select only lines that are long enough
    From which I expect that they are pure text lines and therefore
    relevant for and interpretable by ChatGPT
    :param pdf_file: path to pdf file
    """
    text = extract_text(pdf_file)  # extract text from pdf

    lines = text.split("\n")  # split text into lines
    paragraphs = text.split("\n\n")  # split text into paragraphs

    max_line_length = max([len(line) for line in lines if len(line) < 80])  # get max line length
    paragraph_length = max_line_length * 5  # define paragraph length

    # clean paragraphs to avoid non-informational characters
    cleaned_paragraphs = [re.sub(r'[^a-zA-Z0-9$€ \!\?\.]', '', paragraph) for paragraph in paragraphs]
    cleaned_paragraphs = [paragraph.strip(' ') for paragraph in cleaned_paragraphs]

    filtered_text = [paragraph for paragraph in cleaned_paragraphs if len(paragraph) > paragraph_length]  # filter lines

    return filtered_text
