import os
from sys import *
def DirectoryWatcher(path):
    print("The path is",path)
    flag=os.path.isabs(path)
    #print("Flag::",flag)
    if flag == False:
        path=os.path.abspath(path)

    exists=os.path.isdir(path)

    if exists:
        for folder,subfolders,filenames in os.walk(path):
            print("Current folder is:"+folder)
            for sub in subfolders:
                print("Subfolder:::"+folder+"is:"+sub)
            for fils in filenames:
                print("File inside "+folder+"is:"+fils)
            print(' ')
    else:
        print("Invalid Path")

def main():
    print("Application Name:"+argv[0])

    if(len(argv) !=2):
        print("Error : Invalid number of argguments")
        exit()

    if(argv[1]=="-h") or (argv[1]=="-H"):
        print("This Script Used to traverse specific directory....")

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : ApplicationName AbsolutePath_of_directory....")
        exit()
    try:
        DirectoryWatcher(argv[1])

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception:
        print("Error : Invalid input")


if __name__=="__main__":
    main()