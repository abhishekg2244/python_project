with open("D:\\2026D\\Python\\2026oython\\server2.txt","a+") as f:
    server_list=["dev","qa","uat","prod"]
    for severs in server_list:
        f.write(f"{severs}")

    f.seek(0)

    print(f.read())
