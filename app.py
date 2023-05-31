# This program generates a README.md of a GitHub repository using Generative AI
# The program essentially reads all the relevant files, combine them together and pass an intelligent prompt to the GPT model to generate a README.md file

# Importing the required libraries
import os
import openai
from dotenv import load_dotenv
import tkinter as tk  
from tkinter import filedialog  


load_dotenv()
openai.api_type  = os.getenv("OPENAI_API_TYPE")
openai.api_base = os.getenv("OPENAI_API_BASE")
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_version = os.getenv("OPENAI_API_VERSION")
IGNORE_FILES_LIST = os.getenv("IGNORE_FILES")
IGNORE_DIR_LIST = os.getenv("IGNORE_DIRECTORIES")
README_START =  f'#\n## What is it?\n'

# Set up the GUI  
root = tk.Tk()  
root.title("Directory Uploader")  

def create_input_prompt(code_dir, prompt_length=3200):
    """
        This function creates the input prompt to be sent to the GPT model
    """
    input_prompt = f""

    # read files from the source code directory and all its subdirectories. It should ignore all the files under the IGNORE_FILES_LIST
    for path, subdirs, files in os.walk(code_dir):
        subdirs[:] = [subdir for subdir in subdirs if not (subdir.startswith('.'))]
        for name in files:
            if name not in IGNORE_FILES_LIST and not name.startswith(".") and not os.path.isdir(name):
                with open(os.path.join(path, name), "r") as f:
                    input_prompt += f"\n# {name}\n"
                    input_prompt += f.read()
                    input_prompt += "\n\n"

    input_prompt = input_prompt[:prompt_length]
    input_prompt += "\n\n===================\n" + "README.md:" + "\n"
    input_prompt += "#\n## What is it?\n"
    return input_prompt
  
# Create a function to handle directory selection  
def select_directory():  
    directory = filedialog.askdirectory()  
    if directory:  
        directory_label.config(text=f"Directory selected: {directory}")  
        return create_input_prompt(directory)  
  
# Create a button for selecting a directory  
button = tk.Button(root, text="Select Directory", command=select_directory)  
button.pack(pady=50)  
  
# Create a label for displaying the selected directory  
directory_label = tk.Label(root, text="")  
directory_label.pack() 


def generate_readme(prompt, model="gpt35"):
    prompt = str(prompt)
    messages = [{"role":"system","content":"You are an expert programmer who knows all the coding languages. You will be provided with the code and generate an elaborate README.md file for the code with description about the project, steps for installation with the list of commands to run, usage, license, acknowledgements, dependencies, prerequisites for the project, Tools needed, API Documentation etc."},
        {"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        engine=model,
        messages=messages,
        temperature=0.2, # this is the degree of randomness of the model's output
        max_tokens=4096,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop="===================\n",
    )
    return response


print("Generating README.md file...")
gpt_response = generate_readme(select_directory())


if gpt_response.choices[0].message["content"]:
    with open('README.md', 'w') as f:
        f.write(gpt_response.choices[0].message["content"])

print("Numbers of tokens used: ",gpt_response.usage.total_tokens)

root.mainloop()  

