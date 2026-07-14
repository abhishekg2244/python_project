f1=open("D:/2026D/Python/2026oython/file.txt","r")   # open("","r")
print(f1.read())
f1.close()


f2=open("D:/2026D/Python/2026oython/break.py","a+")   # open("","a")
print(f2.write("\n hELLO aBHSIHEK"))
f2.close()


with open("D:/2026D/Python/2026oython/file.txt","a+") as f:
    print(f.read())
    f.write("/n Hello Abhishek how are you")
    print(f.read())



