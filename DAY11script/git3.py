import subprocess

# Dictionary of Git commands
commands = {
    1: ["git", "--version"],
    2: ["git", "status"],
    3: ["git", "branch"],
    4: ["git", "log", "--oneline"],
    5: ["git", "remote", "-v"]
}


# Function to execute command
def run_command(command):

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(result.stdout)
    else:
        print(result.stderr)


# Main Program
while True:

    print("=" * 35)
    print("      Git Automation Tool")
    print("=" * 35)

    print("1. Git Version")
    print("2. Git Status")
    print("3. Git Branch")
    print("4. Git Log")
    print("5. Git Remote")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 6:
            print("Good Bye! 👋")
            break

        elif choice in commands:
            print(f"\nExecuting: {' '.join(commands[choice])}\n")
            run_command(commands[choice])

        else:
            print("❌ Invalid Choice")

    except ValueError:
        print("❌ Please enter a valid number.")