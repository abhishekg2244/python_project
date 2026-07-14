import json

with open("D:\\2026D\\Python\\2026oython\DAY7\\config.json", "r") as f:
    data = json.load(f)
    print(data)
    print(data["app"])
    print(data["image"])
    print(data["port"])
    print(data["environment"])