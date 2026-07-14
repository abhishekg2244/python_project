# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
#  Range
print("print number from 1 to 10:")


for i in range(1, 11 ):
    print(i)

print("print number from 10 to 1:")
for j in range (10 ,0 ,-1):
    print(j)

#================================
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20

print("table of 2")
for i in range(2 ,22 ,2 ):
 print (i)

#============ odd number 
print("table of 2")
for i in range(1 ,21 ,2 ):
 print (i)

## Table of 7 
# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
# 7 x 5 = 35
# 7 x 6 = 42
# 7 x 7 = 49
# 7 x 8 = 56
# 7 x 9 = 63
# 7 x 10 = 70

table=int(input("number:"))
print (f"table of (table)")
for i in range (1, 11):

    print(f"{table} * {i} = {table*i}")