

import os
from pathlib import Path

def createfolder():
    name=input("tell me your folder name: ")
    p=Path(name)
    if not p.exists():
        p.mkdir()
    else:
        print("folder name is already exist")



def listiningfoldersandfile():
    p=Path("")
    items=(p.rglob("*"))
    for i,v in enumerate(items):
        print(f"{i+1}:{v}")



def updadtefolder():
    oname=input("which folder you want to updadte")
    old_p=Path(oname)
    
    if old_p.exists() and old_p.is_dir():
        n_name=input("tell folder new name")
        new_p=Path(n_name)
        
        if not new_p.exists():
           old_p.rename(new_p)
        
        else:
            print("folder name already exists")
        
    else:
        print("no such folder name exists")


def deletefolder():
    listiningfoldersandfile()
    name=input("which folder you want to delete")
    p=Path(name)
    if p.exists():
        p.rmdir()
    else:
        print("no such folder exists")


def createfile():
    name=input("tell me your file name with extension")
    p=Path(name)
    if not p.exists():
        with open(p,"w")as file: 
            data = (input("tell your file content"))
            file.write(data)
            print("file created sucessfully")
    else:
        print("file is alredy exists")

def readfile():
    listiningfoldersandfile()
    name=input("which file you want to read")
    p=Path(name)
    if p.exists and p. is_file():
        with open(p,"r")as file:
            data=file.read()
            print(data)
        print("file read sucessfully")    
    else:
        print("no such file exists")
        

def updatefile():
    listiningfoldersandfile()
    name=input("which file you want to updadte")
    p=Path(name)
    if p.exists() and p.is_file():
        print("press 1 for updadting the file name :-")
        print("press 2 for overwriting the content :-")
        print("press 3 for appending in file :-")
        check=int(input("tell your response :-"))
        if check==1:
            new_name=input("tell your new name :-")
            new_p=Path(new_name)
            if not new_p.exists():
                p.rename(new_p)
                print("name updadte sucessfully")
            
            else:
                print("this file is allredy exists")
        
        if check==2:
            with open(p,"w")as file:
                data=input("what you want to write")
                file.write(data)
                print("updadte sucessfully")

        if check==3:
            with open(p,"a")as file:
                data=input("what you want to append")
                file.write(""+data)
                print("updadte sucessfully")
                

def deletefile():
    listiningfoldersandfile()
    name=input("which file you want to delete")
    p= Path(name)
    if p.exists() and p.is_file():
        os.remove(p)
        print("file delete sucessfully")
    else:
        print("your file is allredy delete")

while True:   
    print("press 1 for creating a folder")
    print("press 2 for listining files and folders")
    print("press 3 for updating a folders name")
    print("press 4 for deleting a folder")
    print("press 5 for creating a file files")
    print("press 6 for reading a files")
    print("press 7 for updating a files")
    print("press 8 for deleting a files")
    print("press 0 to exist the application")

    res=int(input("tell your response :-"))


    if res==1:
        createfolder()

    if res==2:
        listiningfoldersandfile()

    if res==3:
        updadtefolder()

    if res==4:
        deletefolder()


    if res==5:
        createfile()

    if res==6:
        readfile()
        
    if res==7:
        updatefile()

    if res==8:
        deletefile()
        break
