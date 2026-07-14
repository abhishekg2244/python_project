employee = {
    "Name": "Abhishek",
    "Team": "DevOps",
    "Experience": 5
}



# Name using get()
print(employee.get("Name"))


# Team using get()
print(employee.get("Team"))
# Salary using get()
print(employee.get("Salary"))
# Salary using get() with default value "Not Found"
print(employee.get("Salary", "Not Found") )