import json

server_dict= {
    "NAME": "DEV server",
    "IP" : "192.168.1.10"

}

server_obj = json.dumps(server_dict)
print(server_dict)


print(json)
print(json.__file__)