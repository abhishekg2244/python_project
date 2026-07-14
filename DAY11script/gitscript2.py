# ================================
#       Git Automation Tool
# ================================

# 1. Git Version
# 2. Git Status
# 3. Git Branch
# 4. Git Log
# 5. Git Remote
# 6. Exit

# Enter Choice: 2

# On branch main
# nothing to commit, working tree clean

import  subprocess

print("=" * 30)
print("Git Automation Tool")
print("=" * 30)

print("1. Git Version")
print("2. Git Status")
print("3. Git Branch")
print("4. Git Log")
print("5. Git Remote")
print("6. Exit")



command={
   1: ["git", "--version"],
   2: ["git", "status"],
   3: ["git", "branch"],
   4: ["git", "remote"],
   5: ["git", "log"]
}

choice=int(input("enter your choice : "))


def run_command(choice):
    try:
        # if choice > 6:
        #     print("good bye")
        # else:
            print(f" you selected: {choice}, and command is  {command[choice]} ")
            result=subprocess.run(command[choice],capture_output=True,text=True)
            
            print(result.stdout)
    except ValueError:
        print(result.stderr)
        print("enter valid number")
        

run_command(choice)