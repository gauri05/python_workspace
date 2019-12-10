import sys
print("Hello Python")

print("Demonstration of Command line arguments ")

print("Name of the file", sys.argv[0])

x=sys.argv[1]

y=sys.argv[2]

print("x:", x)

print("y :", y)

ans= int(x)+int(y)

print("Ans :", ans)