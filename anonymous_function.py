print("Defining normal function As...........")
# normal function
def add(val1,val2):
    return val1+val2
value1=10
value2=20
ret=add(value1,value2)
print("Addition is {} with regular function".format(ret))
#defining lambda function
print("defining lambda function............")
ret=lambda val1,val2:val1+val2
ans=ret(value1,value2)
print("Addition is {} with anonymous function".format(ans))