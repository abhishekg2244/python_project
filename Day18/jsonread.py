
import json

with open("python_project/Day18/config.json", "r") as file:
    data = json.load(file)

print(type(data))
print(data["docker_image"])
print(data["port"])
print(data["environment"])