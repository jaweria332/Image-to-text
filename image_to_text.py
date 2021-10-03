# Importing necessary libraries
from PIL import Image
from pytesseract import *

# Importing necessary libraries
from PIL import Image
from pytesseract import *

pytesseract.tesseract_cmd = r'C:\Users\dell\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

img = Image.open("input_img.png")
output = pytesseract.image_to_string(img)
print(output)