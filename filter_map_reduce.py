from functools import reduce

print("Filter map reduce demo")
arr=[10,24,3,45,76,34,23,14]
evenarr=list(filter(lambda no: (no%2==0),arr))
print("List of even number",evenarr)
modarray=list(map(lambda no:no+2,evenarr))
print("List of maparray {} is".format(modarray))
reducearray = reduce(lambda no1,no2:no1+no2,modarray)
print("Reducearray {} is".format(reducearray))