import os
import os.path
import getpass
import shutil
from zipfile import ZipFile
from os import scandir



username=(getpass.getuser())



# PDF documents
def getpdf():
    directory = input("Enter the directory that you want to scan: ")
    directory = directory.strip()
    directory.capitalize()
    documents = [os.listdir(F"/Users/{username}/{directory}")]
    os.chdir(F"/Users/musabhamid/{directory}")
    print(os.getcwd())
    for items in documents:
        for files in items:
            if files.endswith('.pdf'):
                if not os.path.isdir(F"/Users/{username}/{directory}/PDF's"):
                    os.mkdir(F"/Users/{username}/{directory}/PDF's")
                    os.chdir(F"/Users/{username}/{directory}")
                else:
                    os.chdir(F"/Users/{username}/{directory}")
                pdfs = files
                shutil.move(F"/Users/{username}/{directory}/{pdfs}",F"/Users/{username}/{directory}/PDF's/{pdfs}")
                print(F"The following files have been organized: {pdfs}")



def getword():
    directory = input("Enter the directory that you want to scan: ")
    directory = directory.strip()
    directory.capitalize()
    documents = [os.listdir(F"/Users/{username}/{directory}")]
    os.chdir(F"/Users/{username}/{directory}")
    print(os.getcwd())
    for items in documents:
        for files in items:
            if files.endswith('.docx') or files.endswith('doc') or files.endswith('pages'):
                if not os.path.isdir(F"/Users/{username}/{directory}/Word_Documents"):
                    os.mkdir(F"/Users/{username}/{directory}/Word_Documents")
                    os.chdir(F"/Users/{username}/{directory}")
                else:
                    os.chdir(F"/Users/{username}/{directory}")
                worddocs = files
                shutil.move(F"/Users/{username}/{directory}/{worddocs}",F"/Users/{username}/{directory}/Word_Documents/{worddocs}")
                print(F"The following files have been organized: {worddocs}")


def getpic():
    directory = input("Enter the directory that you want to scan: ")
    directory = directory.strip()
    directory.capitalize()
    documents = [os.listdir(F"/Users/{username}/{directory}")]
    os.chdir(F"/Users/{username}/{directory}")
    print(os.getcwd())
    for items in documents:
        for files in items:
            if files.endswith('.png') or files.endswith('jpg') or files.endswith('heic') :
                if not os.path.isdir(F"/Users/{username}/{directory}/Photos"):
                    os.mkdir(F"/Users/{username}/{directory}/Photos")
                    os.chdir(F"/Users/{username}/{directory}")
                else:
                    os.chdir(F"/Users/{username}/{directory}")
                photos = files
                shutil.move(F"/Users/{username}/{directory}/{photos}",F"/Users/{username}/{directory}/Photos/{photos}")
                print(F"The following photos have been organized: {photos}")




userinput = input('Welcome to Smart file! please type which type of files you would like to organize: A for photos, B fpr Word Documents '
                  'and C for PDFs or type d to organize all files,  ')
userinput = userinput.strip()
userinput = userinput.lower()



if userinput == 'a':
    getpic()
elif userinput == 'b':
    getword()
elif userinput == 'c':
    getpdf()
elif userinput == 'd':
    getpic()
    getpdf()
    getword()
elif userinput == 'e':
    extractarchives()


