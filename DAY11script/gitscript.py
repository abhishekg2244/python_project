# =========================
#     Git Automation Tool
# =========================

# 1. Git Version
# 2. Git Status
# 3. Git Branch
# 4. Git Log
# 5. Git Remote
# 6. Exit

# Enter Choice:

import subprocess

print("=" * 30)
print("Git Automation Tool")
print("=" * 30)

print("1. Git Version")
print("2. Git Status")
print("3. Git Branch")
print("4. Git Log")
print("5. Git Remote")
print("6. Exit")

#### take user input for choice
choice = int(input("Enter your choice: "))
print(choice)

### create Dictionary
commands = {
    1: ["git", "--version"],
    2: ["git", "status"],
    3: ["git", "branch"],
    4: ["git", "log", "--oneline"],
    5: ["git", "remote", "-v"],
    6: ["cmd", "/c", "dir"]
}

if choice == 7:
    print("Good Bye!")

elif choice in commands:
    result = subprocess.run(
        commands[choice],
        capture_output=True,
        text=True
    )

    print(result.stdout)

print(type(choice))

print(commands[choice])
print(commands.keys())
print(commands.values())
print(commands.items())