from docxtpl import DocxTemplate
import io

def dictobin(card_dict,template):
    doc = DocxTemplate(f"templates/{template}.docx")
    doc.render(card_dict)
    buffer = io.BytesIO()
    doc.save(buffer)
    return buffer.getvalue()
