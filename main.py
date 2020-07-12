import os
import filetype
import shutil
from os import scandir
os.listdir("/")


def getpdf():
    directory = input("Enter the directory that you want to scan: ")
    documents = [os.listdir(F"/Users/musabhamid/{directory}")]
    directory = directory.strip()
    directory.capitalize()
    for items in documents:
        for files in items:
            if files.endswith('.pdf'):
                pdffiles = files
                print(pdffiles)

def getword():
    directory = input("Enter the directory that you want to scan: ")
    documents = [os.listdir(F"/Users/musabhamid/{directory}")]
    directory = directory.strip()
    directory.capitalize()
    for items in documents:
        for files in items:
            if files.endswith('.doc') or files.endswith('.docx') :
                worddocs = files
                print(worddocs)

def getpic():
    directory = input("Enter the directory that you want to scan: ")
    directory = directory.strip()
    directory.capitalize()
    documents = [os.listdir(F"/Users/musabhamid/{directory}")]
    os.chdir(F"/Users/musabhamid/{directory}")
    print(os.getcwd())

    for items in documents:
        for files in items:
            if files.endswith('.png') or files.endswith('.jpg'):
                os.mkdir(F"/Users/musabhamid/{directory}/Photos")
                os.chdir(F"/Users/musabhamid/{directory}")
                photos = files
                shutil.move(F"/Users/musabhamid/{directory}/{photos}",F"/Users/musabhamid/{directory}/Photos/{photos}")
                print(photos)





getpic()

