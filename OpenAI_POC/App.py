"""
    Run-time instructions 
    
    python3 -m venv venv
    C:\Users\prabh\OneDrive\Documents\OpenAI_POC\venv\Scripts\pip install -r requirements.txt

    Open Command Prompt as administrator 

    cd "C:\Users\prabh\OneDrive\Documents\OpenAI_POC\venv\Scripts"

    activate

    cd "C:\Users\prabh\OneDrive\Documents\OpenAI_POC"

    C:\Users\prabh\OneDrive\Documents\OpenAI_POC\venv\Scripts\flask run

    Open Browser and go to: http://localhost:5000
"""

import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        ai_Prompt = request.form["AI_Prompt"]

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(ai_Prompt),
            temperature=0.6,
        )

        return redirect(url_for("index", result=response.choices[0].text))

    ai_result = request.args.get("result")

    return render_template("index.html", result=ai_result)

def generate_prompt(ai_Prompt):
    return """Suggest three names for an animal that is a superhero.
        Animal: Cat
        Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
        Animal: Dog
        Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
        Animal: {}
        Names:""".format(
                ai_Prompt.capitalize()
    )
