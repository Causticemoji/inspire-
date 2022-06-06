
f=open("lesson1.txt")
f.read()
f.readline()
with open("lesson1.txt",'w')as f:
    f.write("this is my new file\n")
    f.write("i am from ngara\n")
    f.write("today is a cloudy day\n")

print(f.read())
print(f.readline())
f.close()
