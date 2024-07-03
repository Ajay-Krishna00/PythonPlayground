#This is a program to manipulate pdf files using pypdf library

from pypdf import PdfWriter
from os import listdir

contents=listdir('.')           # returns a list containing the names of all files in the directory
pdf=[]
for item in contents:
    if item.endswith(".pdf"):
        pdf.append(item)        #appending all pdf files in the list

merger=PdfWriter()              # Create an instance of PdfWriter class
for item in pdf:
    merger.append(item)
merger.write("Merged_PDF.pdf")  # Write the merged PDF to a new file
merger.close()                  # Close the PdfWriter to release resources