# PDFSearcher.py
# Copyright (c) 02/2019 Vincent Naumann aka. vinmann11

import os.path
from PyPDF2 import PdfFileReader

to_search = input('String to search: ')


def test_pdf(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        pdf_info = pdf.getDocumentInfo()
        pdf_num_pages = pdf.getNumPages()
        pdf_author = pdf_info.author
        pdf_creator = pdf_info.creator
        pdf_producer = pdf_info.producer
        pdf_subject = pdf_info.subject
        pdf_title = pdf_info.title

        pages = []
        for i in range(0, pdf_num_pages):
            # print(pdf.getPage(i).extractText())
            if to_search in pdf.getPage(i).extractText():
                print('File: ' + str(path))
                print('Page: ' + str(i + 1))
                return True

    return False


def found_to_search(dir):
    for file in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, file)):
            if file.endswith('.pdf'):
                if test_pdf(os.path.join(dir, file)):
                    return True
        else:
            found_to_search(os.path.join(dir, file))


found = found_to_search(os.getcwd())
if not found:
    print('String not found')

input()
