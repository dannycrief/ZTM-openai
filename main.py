import os
import openai
from dotenv import load_dotenv
from med_docs import fetch_document, send_openai_request

load_dotenv()

api_key = os.getenv("OPENAI_KEY")
openai.api_key = api_key

model = "text-davinci-003"

if __name__ == "__main__":
    user_input_file = input("Enter file name: ")
    # doc = fetch_document("docs/19_Vermox100.txt")
    doc = fetch_document(user_input_file)
    while True:
        user_input = input("SK: ")
        if user_input == "exit":
            break
        gpt_response = send_openai_request(engine=model, prompt=user_input)
        print("GPT:", gpt_response)
