import os
import io
from PIL import Image
import pytesseract
from wand.image import Image as wi
import openai


def fetch_document(document: str) -> str:
    if not os.path.exists(document):
        raise Exception("ERROR: File does not exist.")
    if ".txt" in document:
        return fetch_txt(document)
    # pdf_text = ""
    # reader = PdfReader(document)
    # print(f"Number of pages: {len(reader.pages)}")
    # for i in range(len(reader.pages)):
    #     page = reader.pages[i]
    #     pdf_text += page.extract_text()
    # print(pdf_text)
    return ""


def fetch_txt(filename_txt: str) -> str:
    fetched_file = open(filename_txt, "r", encoding='utf-8')
    return "".join(fetched_file.readlines()).replace("\n", " ")


def send_openai_request(engine, prompt, max_tokens=1024) -> str:
    response = openai.Completion.create(
        model=engine,
        prompt=prompt,
        temperature=0,
        max_tokens=max_tokens,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["?"]
    )
    return response.choices[0].text.replace("\n", "")
