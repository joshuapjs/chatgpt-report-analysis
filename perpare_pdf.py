from pdfminer.high_level import extract_text


def textcleaner(pdf_file: str):
    """
    Function to select only lines that are long enough
    From which I expect that they are pure text lines and therefore
    relevant for and interpretable by ChatGPT
    :param pdf_file: path to pdf file
    """
    text = extract_text(pdf_file).split('\n')  # split text into lines
    paragraphs = [paragraph for paragraph in text if len(paragraph) > 60]  # select only lines that are long enough

    return paragraphs
