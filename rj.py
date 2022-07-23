import img2pdf
from PIL import Image
import os
from PIL import Image
from pytesseract import pytesseract

#img_path = "C:/Users/FHZ/stage1.png"
  
#pdf_path = "C:/Users/FHZ/file.pdf"
#image = Image.open(img_path)
#pdf_bytes = img2pdf.convert(image.filename)
#file = open(pdf_path, "wb")
#file.write(pdf_bytes)
#image.close()
  

#file.close()
#print("Successfully made pdf file")

path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
image_path = r"C:\Users\FHZ\stage1.png"
  
# Opening the image & storing it in an image object
img = Image.open(image_path)
  
# Providing the tesseract executable
# location to pytesseract library
pytesseract.tesseract_cmd = path_to_tesseract
  
# Passing the image object to image_to_string() function
# This function will extract the text from the image
text = pytesseract.image_to_string(img)
  
# Displaying the extracted text
print(text[:-1])


