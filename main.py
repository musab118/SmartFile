import os
import filetype
import shutil
from os import scandir
os.listdir("/")


def getpdf():
    directory = input("Enter the directory that you want to scan: ")
    documents = [os.listdir(F"/Users/musabhamid/{directory}")]
    directory.strip()
    for items in documents:
        for files in items:
            if files.endswith('.pdf'):
                pdffiles = files
                print(pdffiles)

def getword():
    directory = input("Enter the directory that you want to scan: ")
    documents = [os.listdir(F"/Users/musabhamid/{directory}")]
    directory.strip()
    for items in documents:
        for files in items:
            if files.endswith('.doc') or files.endswith('.docx') :
                worddocs = files
                print(worddocs)

def getpic():
    directory = input("Enter the directory that you want to scan: ")
    documents = [os.listdir(F"/Users/musabhamid/{directory}")]
    directory.strip()
    for items in documents:
        for files in items:
            if files.endswith('.png') or files.endswith('.jpg') :
                photos = files
                print(photos)







