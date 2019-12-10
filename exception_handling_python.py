print("Exception handling in python.....")
no1=int(input("Enter number:"))
no2=int(input("Enter number:"))
try:
    ans=no1/no2
    print("Answer is:::",ans)
except ZeroDivisionError:
    print("Exception ")
finally:
    print("Free allocated resoures")

print("End of Exception handling application")