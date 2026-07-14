import json 

# harcode dict
employee = {
    "Name": "Abhishek",
    "Team": "DevOps",
    "Experience": 5
}

with open("employee.json", "w") as f:
          data_wrtie= json.dump(employee , f)  # ye file likh deta hia
        
          print("file create successfully")

with open("employee.json", "r") as f:
       data_wrtie= json.loads(employee.json)
       data_read=f.read(employee.json)
       print(data_read)


# json.dump() se employee.json file banao.
# json.load() se us file ko read karo.
# Print:
# Name
# Team
# Experience