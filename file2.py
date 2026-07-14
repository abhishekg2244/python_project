with open("D:\\2026D\\Python\\2026oython\\server.txt", "a+") as server_file:
    server_file.write("\n dev")
    server_file.write("\n qa")
    server_file.write("\n uat")
    server_file.write("\n prod")

    server_file.seek(0)  # cursor on top

    print(server_file.read())