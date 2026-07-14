server = {
    "Hostname": "web01",
    "IP": "10.0.0.5",
    "OS": "Ubuntu",
    "Status": "Running"
}

# Task 1
# Print only keys.
for server_key in server:
    print(server_key)

# Task 2
# Print only values.
for server_key in server:
    print(server[server_key])

# Task 3
# Print output exactly like this:
# Hostname : web01
# IP : 10.0.0.5
# OS : Ubuntu
# Status : 
for server_key, server_values in server.items():
    print(server_key, ":", server_values)


# second way 
for server_key, server_values in server.items():
    print(f"{server_key} : {server_values}")