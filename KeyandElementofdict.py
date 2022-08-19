a = {"one":"Monday","Two":"Tuesday","Three":{"A":"Wednesday","B":"Thursday"},"Four":"Friday"}
print(a)
print(a["Four"])
print(a["Three"]["A"])
a["Five"]="Saturday"

print(a)
del(a["Two"])
print(a)
a.update({"one":"Holiday"})
print(a)
print(a.keys())