print("Python Data type demo")

no=None
print(no)
print(type(no))
print(id(no))

no = 11          #int
print(no)
print(type(no))
print(id(no))

no=None             #none
print(no)
print(type(no))
print(id(no))

no = 3.14          #float
print(no)
print(type(no))
print(id(no))

no = 6+3j            #complex
print(no)
print(type(no))
print(id(no))

no = True
print(no)
print(type(no))
print(id(no))

#convert data type from one data type to another data type

no =10

no =float(no)
print(no)

print(type(no))
print(id(no))

no=3.14
no = int(no)
print(no)
print(type(no))
print(id(no))

a=5
b=9

no =complex(a,b)
print(no)
print(type(no))
print(id(no))

print("Demo of List   Tuple    Set    Range")

listX= [14,23,46,78]
print(listX)
print(type(listX))

setX= {23,45,67,78}
print(setX)
print(type(setX))

tupleX= (45,"dfhgdf",89,"DFFG")
print(tupleX)
print(type(tupleX))

str="Demo"
print(str)
print(type(str))

ex = list(range(1,10))
print(ex)
print(type(ex))

ex = list(range(10))
print(ex)
print(type(ex))

ex = list(range(1,10,2))
print(ex)
print(type(ex))

# dictionary  data type
batch = {"PPA":"4000","PPPPP":"900000","777788":"tyyttt"}
print(batch)
print(type(batch))
print(batch.keys())
print(batch.values())
print(batch["PPPPP"])