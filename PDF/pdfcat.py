#! /usr/bin/env python

from PyPDF2 import PdfFileReader, PdfFileWriter
import sys


def merge_pdfs(paths, output):
    """take pdf files defined in array files and concatenate them
    into one PDF with output name output.
    """
    pdf_writer = PdfFileWriter()

    for path in paths:
        pdf_reader = PdfFileReader(path)
        for pagenum in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(pagenum))

    with open(output, "wb") as out:
        pdf_writer.write(out)


if __name__ == '__main__':
    """
    Take files from command line input parameters. The last one is the
    output destination. All others are input files:
      pdfcat.py input1.pdf input2.pdf input3.pdf output.pdf
    """
    inputfiles = sys.argv[1:len(sys.argv)-1]
    outputfile = sys.argv[-1]

    # print("infputfiles: ", inputfiles)
    # print("outputfile: ", outputfile)

    merge_pdfs(inputfiles, outputfile)
