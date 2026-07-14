import os

try:
    pwd=os.getcwd()
    print(pwd)
    for file in os.listdir():
        if file.endswith(".yaml"):
            print(file)

except:
    print("file nhi hai")

finally:
    print("script is successfull")