print("Accept script which accept directory name from user and remove duplicate files from that directory")
from sys import *
import os
import hashlib
import time


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


def findDup(path):
    flag = os.path.isabs(path)

    if flag == False:
        path = os.path.abspath(path)

    exits = os.path.isdir(path)
    dups = {}

    if exits:
        for dirName, subDirs, fileList in os.walk(path):
            print("Current folder is:" + dirName)
            for filen in fileList:
                path = os.path.join(dirName, filen)
                file_hash = hashfile(path)

                if file_hash in dups:
                    dups[file_hash].append(path)
                    print("Append")
                else:
                    dups[file_hash] = [path]
                    print("ADDDD")
        return dups
    else:
        print("Invalid Path")


def printResults(dict1):

    results = list(filter(lambda x: len(x) > 1, dict1.values()))

    if len(results) > 0:
        print("Duplicates found:")
        print("The following files are duplicate")
        for result in results:
            for subresult in result:
                print('\t\t%s' % subresult)
    else:
        print("No duplicates files found.")


def DeleteFiles(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))
    icnt = 0
    if len(results) > 0:
        for result in results:
            print("$$$result:::",result)
            for subresult in result:
                print("####subresult:::",subresult)
                icnt += 1
                if icnt >= 2:
                    os.remove(subresult)
            icnt = 0
    else:
        print("No duplicates files found.")


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
        arr = {}
        startTime = time.time()
        arr = findDup(argv[1])
        printResults(arr)
        DeleteFiles(arr)
        endTime = time.time()

        print('Took %s seconds to evaluate.' % (endTime - startTime))

    except ValueError:
        print("Error : Invalid datatype of input")
    except Exception as E:
        print("Error : Invalid input", E)


if __name__ == "__main__":
    main()
