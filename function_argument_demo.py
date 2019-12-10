print("Python Function Arguments")


# position arguments
def pos(n, f):
    print("Batch name  ", n)
    print("Batch fees  ", f)


# Keyword argument
def keyword_arg(n, f):
    print("Batch name  ", n)
    print("Batch fees  ", f)


# default argument
def default_arg(n, f=7000):
    print("Batch name  ", n)
    print("Batch fees  ", f)


# variable number of argument
def add(*no):
    ans = 0
    for i in no:
        ans = ans + i
    return ans


# keyword variable number of parameter
def stud_info(**info):
    print(info)
    for i,j in info.items():
        print(i,j)


pos('python', 3400)
pos(9000, 'Python')

keyword_arg(n="j,hhgf", f=768687)
keyword_arg(f=98997, n="hgfhdgndn")

default_arg("ngfsdgfj", 90000)
default_arg("PPA")

ret = add(10, 20, 30)
print(ret)

stud_info(age=23, address="Vimannagar", name="Gauri Botre", phoneno=65453656345)
