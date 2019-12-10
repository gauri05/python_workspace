print("String Demo")

s1 = "DemoWith Double Quotes"

s2 = "Demo with single"

print(s1)
print(type(s1))

print(s2)
print(type(s2))

print(s1[0])
print(s1[6])

#accesses right to left
print(s1[-1])
print(s2[-2])

#print a range of character
print(s1[0:3])
print(s1[2:])  # it count from 1 and print the string from 3
print(s1[:3])

#s1[0] = 'm'
print(s1)

print(len(s1)) # also count number of white spaces

# remove white spaces from begining and end
str = " Welcome to new Demo  "
print(str.strip())

print(str)

Batchs = "PPA,LB,Angular,Python,C#,Project,UNIX,LSP"
print(Batchs)
print(Batchs.split(","))




