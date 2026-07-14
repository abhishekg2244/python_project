# ================================
#     Docker Automation Tool
# ================================

# 1. Docker Version
# 2. Docker Images
# 3. Running Containers
# 4. All Containers
# 5. Docker System Info
# 6. Exit

import subprocess

command={
    1: ["docker", "--version"],
    2: ["docker", "images"],
    3: ["docker", "ps"],
    4: ["docker", "ps", "-a"],
    5: ["docker", "system", "info"]
    
}

def docker_command(choice):
    output=subprocess.run(command[choice],
                   capture_output=True,
                   text= True)
    if output.returncode==0:
       print("*" *20)
       print(output.stdout)
       print("*" *20)
    else:
       print("*" *20)
       print(output.stderr)
       print("*" *20)
    
    



while True:

    print("=" * 35)
    print("Docker Automation Tool")  
    print("=" * 35)

    print("1:[docker,--version]")
    print("2:[docker,images]")
    print("3:[docker,ps]")
    print("4:[docker,ps,-a]")
    print("5:[docker,system,info]")
    print("6:exit")

    try:
        user_input=int(input("enter your choice :" ))
    
        if user_input == 6:
            print("exit")
            break 
        elif user_input in command:
            docker_command(user_input)

    except ValueError:
        print("Please enter a valid number.")
    except KeyError:
        print("Invalid Choice")


