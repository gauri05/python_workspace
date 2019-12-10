print("Array demo")
import array as arr
a = arr.array('i', [2, 4, 5, 3, 1])
print("First element",a[1])
print("Last element",a[-1])
print("Second last element",a[-2])

a=arr.array('f', [2.1, 3.4, 5.6])
print("First element",a[1])
print("Last element",a[-1])
print("Second last element",a[-2])
print(a.typecode)
a.reverse()
for i in range(len(a)):
    print(a[i])
i=0
while(i<len(a)):
    print(a[i])
    i+=1