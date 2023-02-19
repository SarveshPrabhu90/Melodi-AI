# OpenAI API POC

This repository contains the POC for the following OpenAI models.

1. Text-davinci-003
2. Text-babbage-001

There are three Python applications used in this POC.
1. App.py which uses the [Flask](https://flask.palletsprojects.com/en/2.0.x/) web framework. Please find the instructions below to setup the [Flask] workflow. 

2. Text-Davinci-003_Chatbot.py - An interactive Chatbot Python application that uses Text-davinci-003 model. 

3. BabbageModel_Chatbot.py - An interactive Chatbot Python application that uses Text-babbage-001 model. 

## Setup Flask workflow

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/)

2. Clone this repository

3. Navigate into the project directory

   ```bash
   $ cd openai-quickstart-python
   ```

4. Create a new virtual environment

   ```bash
   $ python -m venv venv
   $ . venv/bin/activate
   ```

5. Install the requirements

   ```bash
   $ pip install -r requirements.txt
   ```

6. Make a copy of the example environment variables file

   ```bash
   $ cp .env.example .env
   ```

7. Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file

8. Run the app

   ```bash
   $ flask run
   ```

Access the app at [http://localhost:5000](http://localhost:5000).


## Steps to Execute Davinci-003 & Babbage-001 Models 

Navigate to the Project folder

  ```bash
   cd C:\Users\prabh\OneDrive\Documents\OpenAI_POC

   pip install openai
   python.exe -m pip install --upgrade pip

   python BabbageModel_Chatbot.py
   ```




