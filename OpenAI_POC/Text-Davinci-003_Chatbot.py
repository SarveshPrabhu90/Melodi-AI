# Steps to Execute Code 

# Navigate to the Project folder 
# cd C:\Users\prabh\OneDrive\Documents\OpenAI_POC

# pip install openai
# python.exe -m pip install --upgrade pip
# python Text-Davinci-003_Chatbot.py

import openai
import os

# Get API key from environment variable
openai_api_key = os.environ.get("OPENAI_API_KEY")
openai_api_key = "Replace Private Key Here"

# Set up API key
openai.api_key = openai_api_key

# Use the Text-Davinci-003 model for completion
model_engine = "text-davinci-003"

print("Hello! I am a AI program by OpenAI. My model is: Text-Davinci-003 model. \nHow may I help you today?")

while True:
    # Get user input
    user_input = input("You: ")
    
    if user_input.strip() == "Exit":
        print("Goodbye! Have a great day.")
        break

    """
        The n parameter in OpenAI API specifies the number of completions to generate for a given prompt. 
        Each completion is a continuation of the prompt text, generated by the model. 
        For example, if n=3, then three different completions for the same prompt will be generated.

        The temperature parameter in OpenAI API controls the level of randomness in the generated text. 
        It's a value between 0 and 1, where a low temperature (e.g. 0.1) will result in more conservative, predictable responses, 
        while a high temperature (e.g. 1) will result in more diverse, unpredictable responses.

        A temperature of 0 will result in the model always choosing the most likely token at each step, 
        while a temperature of 1 will allow the model to randomly sample from the distribution of all tokens, 
        potentially generating novel or unexpected responses.

        In practice, temperatures between 0.3 and 0.7 are often used to achieve a good balance 
        between conservatism and diversity in the generated text. 
    """
    
    # Use the Text-Davinci-003 model for completion
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=user_input,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    
    # Get the first completion result
    message = completion.choices[0].text
    
    # Print the AI's response
    print(f"AI: {message}")

