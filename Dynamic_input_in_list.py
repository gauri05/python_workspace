print("Dynamic input in List")
arr=list()
num=input("Enter how many numbers you want::::")
print("Enter the number in array")
for i in range(0,int(num)):
    no=input("num:")
    arr.append(int(no))
print("The List is :::",arr)