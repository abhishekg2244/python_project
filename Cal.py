# Enter First Number: 20
# Enter Second Number: 10

# Enter Operation (+, -, *, /): *

# Result: 200


fn= int(input("enter fn number : "))
sn= int(input("enter sn number: "))


choose_operator= input(f"choose operator: +, - , * , /  :")


if choose_operator == "+":
    print(f"{fn}+{sn}: {fn+sn}")

elif choose_operator == "-":
    print(f"{fn}-{sn}:{fn-sn}")

elif choose_operator == "*":
    print(f"{fn}*{sn}:{fn*sn}")

elif choose_operator == "/":
    if sn == 0:
      print("Division by zero is not allowed.20")

    else:
      print(f"{fn}/{sn}:{fn/sn}")

else:
    print("invalid operator")


