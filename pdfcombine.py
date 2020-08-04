import PyPDF2
import sys

imports = sys.argv[1:]


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for file in pdf_list:
        merger.append(file)
    merger.write('newpdf.pdf')


pdf_combiner(imports)
