print("Python Object Orientation")
class Demo:
    def __init__(self,value1,value2):  #init is work same as constructor
        print("Inside init method")
        self.i=value1
        self.j=value2
    def fun(self):#self is used to access the methods and attributes of the class
        print ("Inside fun")
        print (self.i,self.j)
    def Add(self):
        print (self.i+self.j)
obj1=Demo(10,20)
obj1.fun()
obj1.Add()
obj2=Demo(2,3)
obj2.fun()
obj2.Add()