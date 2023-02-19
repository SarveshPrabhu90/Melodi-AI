# Steps to Execute Code 

# Navigate to the Project folder 

# pip install openai
# python.exe -m pip install --upgrade pip
# python BabbageModel.py

import openai
import os

# Set up API key
# Get API key from environment variable
openai_api_key = os.environ.get("OPENAI_API_KEY")

openai_api_key = "Replace Private Key Here"

openai.api_key = openai_api_key

# Get prompt from user
prompt = input("Enter your prompt: ")

# Use the Text-Babbage-001 model for completion
model_engine = "text-babbage-001"

completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

# Get the first completion result
message = completion.choices[0].text
print(message)

"""
    # Use the Text-Babbage-001 model for completion
    model_engine = "text-babbage-001"
    prompt = "What is the capital of"

    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Get the first completion result
    message = completion.choices[0].text
    print(message)

"""
