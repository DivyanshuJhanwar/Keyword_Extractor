import pytesseract
from PIL import Image
import os

class OCREngine:
    @staticmethod
    def extract_text(file_path):
        try:
            # Set the path to the Tesseract executable
            pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

            # Open image file
            image = Image.open(file_path)

            # Extract text from the image
            text = pytesseract.image_to_string(image)

            # Return the extracted text as a result
            return text
        except Exception as e:
            return str(e)
