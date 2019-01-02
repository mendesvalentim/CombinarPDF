# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

import os
import glob
import pprint
from PyPDF2 import PdfFileReader, PdfFileMerger

PASTA_FINAL = 'PDFs combinados'
if not os.path.isdir(PASTA_FINAL):     
    os.mkdir(PASTA_FINAL)


def junta_arquivos_pdf(pdfs, nome_pdf_gerado):
    merger = PdfFileMerger()
    for pdf in pdfs:
       merger.append(PdfFileReader(pdf, "rb"))
    merger.write(os.path.join(PASTA_FINAL, nome_pdf_gerado))


def main():
    agrupamento = {}
    print('Separando arquivos para combinação')    
    for nome_arquivo_pdf in glob.glob("*.pdf"):
        numero = nome_arquivo_pdf.split('-')[0].strip()
        if agrupamento.has_key(numero):
            agrupamento[numero].append(nome_arquivo_pdf)
        else:
            agrupamento[numero] = []
            agrupamento[numero].append(nome_arquivo_pdf)
    for numero in agrupamento.keys():
        nome = nome_arquivo_pdf.split('-')[1].strip()
        mes  = nome_arquivo_pdf.split('-')[2].split('.')[0]
        nome_arquivo_novo = '{0} - {1} - {2}.pdf'.format(numero, nome, mes)
        print('Agrupando arquivo: {0}'.format(nome_arquivo_novo))
        junta_arquivos_pdf(agrupamento[numero], nome_arquivo_novo)


if __name__ == "__main__":
    main()