from   PIL import Image
import pytesseract

TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH 


img = Image.open('images/example2.png')
txt = pytesseract.image_to_string(img)
print(txt)