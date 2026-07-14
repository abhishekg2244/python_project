# 1. User se do numbers lo.
# 2. Pehle number ko dusre se divide karo.
# 3. Agar second number 0 ho:
#       "Cannot divide by zero"
# 4. Agar user number ki jagah text likhe:
#       "Please enter valid numbers"
# 5. Agar sab sahi ho:
#       "Division Successful"
# 6. Finally:
#       "Program End"

try:
    fn=int(input("enter first nummber:"))
    sn=int(input("enter second nummber:"))
    result=fn/sn
    print(result)

except ZeroDivisionError:
   print("Cannot divide by zero")

except ValueError:
   print("Please enter valid numbers")

else:
   print("Division Successful")

finally:
   print("Program End")
   


