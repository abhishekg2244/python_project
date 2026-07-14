with open("servers.txt","a+") as file_write:
    servers = ["dev", "qa", "uat", "prod"]
    
    for server in servers:
        file_write.write(f"{server} \n")
        
    file_write.seek(0)

    print(file_write.read())