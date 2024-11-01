#Ejercicio 1 - Con los archivos pedidos en diferentes formatos (pdf, jpg, …otros) la
#clase anterior, extraiga la información que considere relevante de los mismos
#utilizando las librerías desarrolladas en clase.

#i. Obtenga texto de un libro escaneado en pdf (un pdf que no tenga el texto
#codificado como tal, es decir, que sea necesario usar ocr). Pruebe usando
#pytesseract en ingles (por defecto) y luego configurándolo en español.

#ii. Obtenga texto de una imagen (png, bmp).

#iii. Obtenga texto de un archivo word.

#iv. Obtenga texto de un archivo de audio.

#----------------------------------------------------------------------------------------------

#i

from PIL import Image
import pytesseract
from pdf2image import convert_from_path
import os

pop_path = r"C:\Users\sonop\Desktop\TUIA\2do año\Cuatrimestre 2\NLP\poppler-24.07.0\Library\bin"

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

archivo_imagen = "imagenes-pdf/archivo-de-pdf.pdf"

imagenes = convert_from_path(archivo_imagen, poppler_path=pop_path)

carpeta = "imagenes-pdf"


for i, imagen in enumerate(imagenes):
    ruta_carpeta_imagenes = os.path.join(carpeta, 'pagina{}.png'.format(i))

    imagen.save(ruta_carpeta_imagenes,'PNG')


for i, imagen in enumerate(imagenes):
    archivo = 'pagina{}.png'.format(i)
    ruta_guardado = os.path.join(carpeta, archivo)
    
    if os.path.exists(ruta_guardado):
        continue
    else:
        imagen.save(ruta_guardado, 'PNG')
        


ruta_carpeta = "imagenes-pdf"

nombre_imagen = "pagina2.png"

ruta_imagen = os.path.join(ruta_carpeta, nombre_imagen)

imagen = Image.open(ruta_imagen)


texto = pytesseract.image_to_string(imagen)

print(texto)

