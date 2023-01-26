import os
import openai
from dotenv import load_dotenv
from med_docs import fetch_document, send_openai_request

load_dotenv()

api_key = os.getenv("OPENAI_KEY")
openai.api_key = api_key

doc = fetch_document("docs/19_Vermox100.txt")

prompt = doc
model = "text-davinci-003"
while True:
    # Get the user's input
    user_input = input("SK: ")
    if user_input == "exit":
        break
    # Generate a response from GPT-3
    completions = send_openai_request(engine=model, prompt=user_input)
    gpt_response = completions.choices[0].text
    print("GPT:", gpt_response.replace("\n\n", ""))
