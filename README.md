# chatgpt-report-analysis
A simple tool to make financial reports digestable. Utilize the capabilities of OpenAI's API to read the text of PDFs of a Financial Report and ask your question about it to get an overview and save time.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python Version**: Python 3.x
- **Python Libraries**:
  - `openai`
  - `tiktoken`
  - `pdfminer.six`
- **API Access**: An access key for the OpenAI API.

## Setup

- Store your OpenAI API key in an environment variable named `OPENAI_API_KEY`.
- Adjust the parameters accordingly in the `variables.py` file for:
  - **"model"**
  - **"request_size"**
  - **"answer_size"**
  - **"question"**  

## Feature

Get ChatGPT to answer your **"question"** about the text in the Financial Report.

## Usage

### Run the package through your terminal

Please make sure to change *"path"* to the path of the PDF file you want to analyze.

```bash
python3 -m chatgpt-report-analysis "path"
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

Ensure you comply with the terms of use of OpenAI API when using this tool. The tool and its functions were designed for educational purposes and may require further refinement for production use.
