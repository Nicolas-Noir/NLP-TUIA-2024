from PIL import Image
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

carpeta = "imagenes-todas"

archivo_imagen = 'claymore.jpg'

ruta = os.path.join(carpeta, archivo_imagen)

imagen = Image.open(ruta)

texto = pytesseract.image_to_string(imagen, lang="eng")

print(texto)