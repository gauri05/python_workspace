print("Python object oriented Character")
class Demo:
    x=10
    def __init__(self,no1,no2):
        self.i=no1
        self.j=no2
obj1=Demo(100,200)
obj2=Demo(1,2)
print(obj1.i)
print(obj1.j)
print(obj2.i)
print(obj2.j)
print(Demo.x)