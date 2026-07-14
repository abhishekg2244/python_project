import json

server = {
    "Hostname": "web01",
    "IP": "10.0.0.5",
    "OS": "Ubuntu",
    "Status": "Running"
}

print(server)
print(type(server))

json_object = json.dumps(server)

print(json_object)
print(type(json_object))