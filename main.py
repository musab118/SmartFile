import os
import filetype
import shutil
from os import scandir
os.listdir("/")




def getpdf():
    directory = input("Enter the directory that you want to scan: ")
    directory = directory.strip()
    directory.capitalize()
    documents = [os.listdir(F"/Users/musabhamid/{directory}")]
    os.chdir(F"/Users/musabhamid/{directory}")
    print(os.getcwd())
    for items in documents:
        for files in items:
            if files.endswith('.pdf'):
                if not os.path.isdir(F"/Users/musabhamid/{directory}/PDF's"):
                    os.mkdir(F"/Users/musabhamid/{directory}/PDF's")
                    os.chdir(F"/Users/musabhamid/{directory}")
                else:
                    os.chdir(F"/Users/musabhamid/{directory}")
                pdfs = files
                shutil.move(F"/Users/musabhamid/{directory}/{pdfs}",F"/Users/musabhamid/{directory}/PDF's/{pdfs}")
                print(F"The following files have been organized: {pdfs}")


def getword():
    directory = input("Enter the directory that you want to scan: ")
    directory = directory.strip()
    directory.capitalize()
    documents = [os.listdir(F"/Users/musabhamid/{directory}")]
    os.chdir(F"/Users/musabhamid/{directory}")
    print(os.getcwd())
    for items in documents:
        for files in items:
            if files.endswith('.docx'):
                if not os.path.isdir(F"/Users/musabhamid/{directory}/Word_Documents"):
                    os.mkdir(F"/Users/musabhamid/{directory}/Word_Documents")
                    os.chdir(F"/Users/musabhamid/{directory}")
                else:
                    os.chdir(F"/Users/musabhamid/{directory}")
                worddocs = files
                shutil.move(F"/Users/musabhamid/{directory}/{worddocs}",F"/Users/musabhamid/{directory}/Word_Documents/{worddocs}")
                print(F"The following files have been organized: {worddocs}")


def getpic():
    directory = input("Enter the directory that you want to scan: ")
    directory = directory.strip()
    directory.capitalize()
    documents = [os.listdir(F"/Users/musabhamid/{directory}")]
    os.chdir(F"/Users/musabhamid/{directory}")
    print(os.getcwd())
    for items in documents:
        for files in items:
            if files.endswith('.png'):
                if not os.path.isdir(F"/Users/musabhamid/{directory}/Photos"):
                    os.mkdir(F"/Users/musabhamid/{directory}/Photos")
                    os.chdir(F"/Users/musabhamid/{directory}")
                else:
                    os.chdir(F"/Users/musabhamid/{directory}")
                photos = files
                shutil.move(F"/Users/musabhamid/{directory}/{photos}",F"/Users/musabhamid/{directory}/Photos/{photos}")
                print(F"The following files have been organized: {photos}")




userinput = input('Welcome to Smart file! please type which type of files you would like to organize: ')
userinput = userinput.strip()


if userinput == 'photos':
    getpic()
elif userinput == 'word':
    getword()
elif userinput == 'pdf':
    getpdf()

