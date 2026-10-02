from docxtpl import DocxTemplate,InlineImage
from docx.shared import Mm

def doctpl(template='Karta.docx',output='output.docx'):
    doc = DocxTemplate(template)
    indeks = 999
    date_updated = '2026-09-29'
    date_fill = '2026-09-28'
    updated_by = 'paw'
    created_by = 'paw'
    name_pl = 'Polska'
    name_eng = 'Anglia'
    image = InlineImage(doc,'1.png',width=Mm(40))
    images = [image for i in range(0,6)]
    context = {
        'indeks' : indeks,
        'date_updated' : date_updated,
        'date_fill' : date_fill,
        'updated_by' : updated_by,
        'created_by' : created_by,
        'name_pl' : name_pl,
        'name_eng' : name_eng,
        'images' : images
    }
    doc.render(context)
    doc.save(output)
