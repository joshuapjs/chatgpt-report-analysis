# chatgpt-report-analysis
A simple tool to make financial reports digestible. Utilize the capabilities of OpenAI's API to read the text of Financial Reports (PDF) and ask your question about it to get an overview and save time.

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
- For further details please visit [OpenAI API](https://platform.openai.com/docs/models/overview)

## Feature

Get the model to answer your **"question"** about the text in the Financial Report.

## Usage

### Run the package through your terminal

Please make sure to change *"path"* to the path of the PDF you want to ask the model about.

```bash
python3 -m chatgpt-report-analysis "path"
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

Ensure you comply with the terms of use of OpenAI's API when using this tool. The tool and its functions were designed for educational purposes and may require further refinement for production use.
