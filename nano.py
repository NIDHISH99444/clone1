import  webbrowser
import os

def renameList():
    # fileList= os.listdir(r"C:\Users\andidwan\Desktop\images")
    # print(fileList)
    fileList=os.listdir(r"C:\Users\andidwan\Desktop\images")
    savedPath=os.getcwd()

    p=os.chdir(r"C:\Users\andidwan\Desktop\images")

    remove="123456789"
    table=str.maketrans("","",remove)
    for file_name in fileList:
        os.rename(file_name,file_name.translate(table))
    os.chdir(savedPath)


renameList()
