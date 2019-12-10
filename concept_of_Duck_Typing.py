print("---- Marvellous Infosystems by Piyush Khairnar-----")
#print("Demonstration of Duck Typing”)
class Sparrow:
    def fly(self):
        print("Sparrow flying")
class Airplane:
    def fly(self):
        print("Airplane flying")
class Whale:
        def swim(self):
            print("Whale swimming")

    # The type of entity is not specified
    # We expect entity to have a callable named fly at run time
def fun(entity):
    entity.fly()

sparrow = Sparrow()
airplane = Airplane()
whale = Whale()
fun(sparrow)  # prints `Sparrow flying`
fun(airplane)  # prints `Airplane flying`
fun(whale)  # Throws the error `'Whale' object has no attribute 'fly'`