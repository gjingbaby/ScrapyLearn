from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_file = open(r"E:\pyworkspace\市县国土空间规划分区与用途分类指南（试行，送审稿）.pdf","rb")

#构造instance
pdf_reader = PdfFileReader(pdf_file)

pdf_writer = PdfFileWriter()

pdf_writer.addPage(pdf_reader.getPage(1))
pdf_writer.addPage(pdf_reader.getPage(4))
pdf_writer.addPage(pdf_reader.getPage(5))


spilt_file = open(r"E:\pyworkspace\哈哈哈.pdf","wb")

pdf_writer.write(spilt_file)

pdf_file.close()
spilt_file.close()
