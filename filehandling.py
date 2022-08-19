f = open("sample.txt","r+")
print(f.read())

print(f.tell())
print(f.readline())
print(f.tell())
f.seek(50)
print(f.readline())
print(f.tell())

f.close()