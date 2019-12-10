from time import *
from os import *
from multiprocessing import *
from threading import *


def Square(no):
    print("Parent_id::", getpid())
    return no * no


def main():
    arr = [1, 31, 41, 2, 4, 6, 7]
    brr = []

    starttime1 = time()
    for i in range(len(arr)):
        brr.append(Square(arr[i]))
    endtime1 = time()

    print(brr)
    print("Serial:", endtime1 - starttime1)

    pobj = Pool()

    starttime2 = time()
    crr = pobj.map(Square, arr)
    endtime2 = time()
    print(crr)
    print("Parallel:::", endtime2 - starttime2)

if __name__ == "__main__":
    main()