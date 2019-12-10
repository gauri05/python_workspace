def sub(no1,no2):
    return no1-no2;
def Decorator(OriginalFunction):
    def Updator(a,b):
        if(a<b):
            a,b=b,a;
        return OriginalFunction(a,b);
    return Updator
newsub = Decorator(sub);
print("Subtraction of 10 and 7 is",newsub(10,7));
print("Subtraction of 7 and 10 is",newsub(7,10));