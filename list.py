# servers = ["dev", "qa", "uat"]
# servers = ["dev", "qa", "uat"]

# Perform these operations:

# Print first server
# Print last server
# Add "prod" using append()
# Add "dr" at index 2 using insert()
# Remove "qa"
# Remove last item using pop()
# Print total number of servers
# Print all servers using a for loop

servers = ["dev", "qa", "uat"]
print(servers[0])
print(servers[1])
print(servers[2])

servers.append("prod")
print(servers)

servers.insert(2,"dr")
print(servers)

servers.remove("qa")
print (servers)

servers.pop()
print (servers)

print(len(servers))

for server in servers:
    print(server)


