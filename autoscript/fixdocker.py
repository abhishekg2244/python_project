import subprocess

commands = {
    1: ["docker", "--version"],
    2: ["docker", "images"],
    3: ["docker", "ps"],
    4: ["docker", "ps", "-a"],
    5: ["docker", "system", "info"]
}


def docker_command(choice):
    output = subprocess.run(
        commands[choice],
        capture_output=True,
        text=True
    )

    if output.returncode == 0:
        print("*" * 30)
        print(output.stdout)
        print("*" * 30)
    else:
        print("*" * 30)
        print(output.stderr)
        print("*" * 30)


while True:

    print("=" * 35)
    print("Docker Automation Tool")
    print("=" * 35)

    print("1. Docker Version")
    print("2. Docker Images")
    print("3. Running Containers")
    print("4. All Containers")
    print("5. Docker System Info")
    print("6. Exit")

    try:
        user_input = int(input("Enter your choice: "))

        if user_input == 6:
            print("Good Bye!")
            break

        elif user_input in commands:
            docker_command(user_input)

        else:
            print("Invalid Choice")

    except ValueError:
        print("Please enter a valid number.")