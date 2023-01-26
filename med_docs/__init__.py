from typing import List, Any

from pypdf import PdfReader
import os
import io
from PIL import Image
import pytesseract
from wand.image import Image as wi
import gc
import openai


def fetch_document(document: str):
    if ".txt" in document:
        return fetch_txt(document)
    # pdf_text = ""
    # reader = PdfReader(document)
    # print(f"Number of pages: {len(reader.pages)}")
    # for i in range(len(reader.pages)):
    #     page = reader.pages[i]
    #     pdf_text += page.extract_text()
    # print(pdf_text)
    text = get_text_from_image(pdf_path=document)
    print(text)


def fetch_txt(filename_txt: str) -> str:
    fetched_file = open(filename_txt, "r", encoding='utf-8')
    return "".join(fetched_file.readlines())


def get_text_from_image(pdf_path: str) -> list[str]:
    pdf_file = wi(filename=pdf_path, resolution=1024)
    pdf_img = pdf_file.convert('jpeg')
    img_blobs = []
    extracted_text = []
    for img in pdf_img.sequence:
        page = wi(image=img)
        img_blobs.append(page.make_blob('jpeg'))

    for imgBlob in img_blobs:
        im = Image.open(io.BytesIO(imgBlob))
        text = pytesseract.image_to_string(im, lang='pl')
        extracted_text.append(text)

    return extracted_text


def send_openai_request(engine, prompt, max_tokens=1024):
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.5
    )
    return response
