# JSON file read karo.
# docker_image ki value "myapp:v2" kar do.
# Usi file me wapas save kar do.

import json

with open("python_project/Day18/config.json", "r") as file:
    data = json.load(file)

data["docker_image"] = "myapp:v2"

with open("python_project/Day18/config.json", "w") as file:
    json.dump(data, file, indent=4)

print("Docker image updated successfully.")