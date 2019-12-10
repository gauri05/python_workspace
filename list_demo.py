print("Python List Demo")
batchs = ["PPA","LB","MultiOS","Angular","Python"]

print(batchs)
print(batchs[0])
print(batchs[1])
print(batchs[-1])
print(batchs[-2])
print(batchs[1:])
print(batchs[2:])
print(batchs[:3])

print("Start for heterogenious data")
data1 = [11,"XYZ",9.14]
print(data1)

data2 = [45,"GHJ",7.34]

combined = [data1,data2]

print(combined)

batchs.append(".net")
print(batchs)

batchs.insert(2,"Project Mag")
print(batchs)

batchs.remove("MultiOS")
print(batchs)

batchs.pop()
print(batchs)


batchs.pop(2)
print(batchs)

del batchs[1:]
print(batchs)

batchs.extend(["LB","MultiOS","Angular","MEAN"])
print(batchs)

batchs.sort()
print(batchs)
