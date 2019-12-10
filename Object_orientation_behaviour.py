print("Object Orientation Behaviour======>>>>>>Instance ===>Static ====>Class")
class Demo:
    def __init__(self):
        self.i=0
        self.j=0
    def fun(self):
        print ("Inside instance")
    @classmethod
    def gun(cls):
        print ("Inside Class method")
    @staticmethod
    def sun():
        print ("Inside Static")
obj1 = Demo()
obj1.fun()
Demo.gun()
Demo.sun()