
f = open("trial.txt","a")
f.write("A new line now")
f.close()
f = open("trial.txt","r")
print(f.read())