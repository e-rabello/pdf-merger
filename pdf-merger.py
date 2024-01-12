from pypdf import PdfMerger

pdfs = ['document-page0.pdf', 'document-page1.pdf']

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()