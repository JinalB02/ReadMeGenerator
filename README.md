# README.md Generator using Generative AI

This program generates a README.md file for a GitHub repository using Generative AI. The program essentially reads all the relevant files, combines them together, and passes an intelligent prompt to the GPT model to generate a README.md file.

## Installation

To install the required libraries, run the following command:

```
pip install -r requirements.txt
```

## Usage

To generate a README.md file for your GitHub repository, run the following command:

```
python extension.py <code_dir>
```

where `<code_dir>` is the path to the directory containing your code.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

This project was made possible thanks to the [OpenAI API](https://beta.openai.com/docs/).

## Dependencies

This program requires the following libraries:

- `os`
- `openai`
- `dotenv`

## Prerequisites

Before running this program, you will need to set up an OpenAI API key. You can follow the instructions [here](https://beta.openai.com/docs/api-reference/authentication) to obtain your API key.

## Local Setup

To set up this program locally, follow these steps:

1. Clone this repository to your local machine.
2. Set up a virtual environment using `virtualenv` or `conda`.
3. Install the required libraries using the command `pip install -r requirements.txt`.
4. Set up your OpenAI API key by creating a `.env` file and adding the following lines:

```
OPENAI_API_KEY=<your_api_key>
OPENAI_API_BASE=https://api.openai.com
OPENAI_API_VERSION=v1
IGNORE_FILES=<comma_separated_list_of_files_to_ignore>
```

5. Replace `<your_api_key>` with your actual OpenAI API key.
6. Replace `<comma_separated_list_of_files_to_ignore>` with a comma-separated list of files to ignore (e.g., `config.ini,.env`).

## API Documentation

This program uses the OpenAI API to generate a README.md file. You can find the documentation for the API [here](https://beta.openai.com/docs/api-reference/introduction).
