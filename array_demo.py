print("Array Demo")

import array as arr

a=arr.array('i',[2,4,5,1])
print("First element",a[0])
print("Second last element",a[-1])

print(a.typecode)

a=arr.array('f',[3.12,4.35,4.67,1.14])
print("First element",a[0])
print("Second last element",a[-1])

print(a.typecode)

a.reverse()
for i in range(len(a)):
    print(a[i])

b= ('k',[5,2,7,9])
for i in range(len(b)): print(b[i])

i=0
while(i<len(b)):
    print(b[i])
    i+=1