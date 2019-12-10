def Sub(no1, no2):
    ans = no1 - no2
    print("Ans", ans)
    return ans;


def Decorator(OriginalFunction):
    def Upator(a, b):
        if (a < b):
            a, b = b, a
            print("A____", a, b)
            print("ORIFUN........", OriginalFunction)
        return OriginalFunction(a,b)

    print("OuterFun........", OriginalFunction)
    return Upator


print("Python Decorator.....")
newsub = Decorator(Sub)
print(newsub(10, 7))
print("Subtraction of 10 and 7 is........", newsub(7, 10))
