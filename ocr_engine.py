# This library is used for optical character recognition (ocr) to extract text from images.
import pytesseract
from PIL import Image   # This library is used to open and manipulate images
import os

class OCREngine:
    @staticmethod
    def extract_text(file_path):
        try:
            image = Image.open(file_path)    # open image file
            text = pytesseract.image_to_string(image)   # extract text from image
            return text     # The extracted text is returned as a result
        except Exception as e: 
           return str(e)