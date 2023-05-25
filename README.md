# Generative AI README.md Generator

This project is a Python program that uses Generative AI to automatically generate a README.md file for a GitHub repository. The program reads all relevant files in the repository, combines them together, and passes an intelligent prompt to a GPT model to generate a comprehensive README.md file.

## Installation

To use this program, you will need to have Python 3.x installed on your computer. You will also need to install the following libraries:

- OpenAI
- dotenv

You can install these libraries by running the following command in your terminal:

```
pip install openai dotenv
```

## Usage

To use this program, you will need to provide the path to the GitHub repository you want to generate a README.md file for. You can do this by modifying the `code_dir` variable in the `create_input_prompt()` function.

Once you have set the `code_dir` variable, you can run the program by executing the following command in your terminal:

```
python extension.py
```

The program will automatically read all relevant files in the repository, generate an intelligent prompt, and use a GPT model to generate a comprehensive README.md file.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## Dependencies

This program depends on the following libraries:

- OpenAI
- dotenv

## Prerequisites

Before using this program, you should have a basic understanding of Python programming and the GitHub repository structure.

## Local Setup

To set up this program locally, you will need to:

1. Clone the GitHub repository to your local machine.
2. Install the required libraries (OpenAI and dotenv) using the `pip install` command.
3. Set the `code_dir` variable in the `create_input_prompt()` function to the path of the GitHub repository you want to generate a README.md file for.
4. Run the program using the `python readme_generator.py` command.

## API Documentation

This program does not have any API documentation.
