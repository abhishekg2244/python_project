employee = {
    "Name": "Abhishek",
    "Age": 32
}



# Add "Team": "DevOps" using update()
employee.update({"Team": "DevOps"})
print(employee)
# Add "Location": "Noida" using update()
employee.update({"Location": "Noida"})
print(employee)
# Change Age to 33
employee.update({"Age": "33"})
print(employee)
# Remove "Location" using pop()
employee.pop("Location")
print(employee)
# Print final dictio
print(employee)