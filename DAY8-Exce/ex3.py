try:
    a = int(input("Enter a number: "))
    c = 10 / a
    print(c)

except ZeroDivisionError:
    print("0 se divide nahi kar sakte.")

except ValueError:
    print("Please numbers hi enter karo.")

