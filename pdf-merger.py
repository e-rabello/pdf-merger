from pypdf import PdfMerger

# add as many files as you want
pdfs = ['document-page0.pdf', 'document-page1.pdf', 'document-page2.pdf']

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

# resulting file
merger.write("result.pdf")
merger.close()
