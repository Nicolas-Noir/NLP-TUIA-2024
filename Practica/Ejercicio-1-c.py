from docx import Document

doc = Document('imagenes-todas/resumen.docx')

for parrafo in doc.paragraphs:
    print(parrafo.text)
