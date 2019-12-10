from sys import *
import os
import hashlib


def hashfile(path, blocksize=1024):
    afile = open(path, 'rb')
    # print("PATH HH::::",path)
    hasher = hashlib.md5()

    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    # print("BUF   " + )
    afile.close()
    return hasher.hexdigest()


def DisplayChecksum(path):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)
    exits = os.path.isdir(path)

    if exits:
        for dirName, subdirs, fileList in os.walk(path):
            print("Current floder is:" + dirName)
            for filen in fileList:
                path = os.path.join(dirName, filen)
                file_hash = hashfile(path)
                print("File name is :"+file_hash)
        #print("Error : Invalid number of argumnets")
        #exit()
    if argv[1] == "-h" or argv[1] == "_H":
        print("This Script is used to traverse specific diretory ")
        exit()
    if argv[1] == "-u" or argv[1] == "-U":
        print("Usage : Applicationname AbsolutePath_of_Directory")
        exit()


def main():
    print("Application name:" + argv[0])

    if len(argv) != 2:
        print("Error : Invalid number of arguments")
        exit()
    if argv[1] == "-h" or argv[1] == "_H":
        print("This Script is used to traverse specific diretory and display checksum of files")
        exit()
    if argv[1] == "-u" or argv[1] == "-U":
        print("Usage : Applicationname AbsolutePath_of_Directory Extention")
        exit()
    try:
        arr = DisplayChecksum(argv[1])
    except ValueError:
        print("Error : Invalid datatype of input")
    except Exception as E:
        print("Error : Invalid input", E)


if __name__ == "__main__":
    main()
