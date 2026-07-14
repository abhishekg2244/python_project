import os

# check current directory

pwd=os.getcwd()
print(pwd)  # print path
print(type(pwd))   # print pwd ka type

list_dir=os.listdir()
print(list_dir)
print(type(list_dir))


for file in list_dir:
    if file.endswith(".py"):
        print(file)
        
        
    
