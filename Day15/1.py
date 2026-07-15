import subprocess

class GitAutomation:
        def __init__(self):
            self.commands={
                1 : ["git" ,"--version"],
                2 : ["git", "status"],
                3 : ["git", "branch"],
                4 : ["git", "log" ,"--oneline"],
                5 : ["git" ,"remote" ,"-v"],
                6 : ["git", "pull"],
                7 : ["git", "push"],
                8 :["git", "add", "."],
                # 9 :[]"git,commit, -m putmsg"],
                9 : ["exit"]
            }

        def show_menu(self):
            
            print("1 : git --version")
            print("2 :git status")
            print("3 :git branch")
            print("4 :git log --online")
            print("5 :git remote -v")
            print("6 :git pull")
            print("7 :git push")
            print("8 :git add .")
            # print("9: git commit -m putmsg")
            print("10: Exit")

        def show_header(self):
            print("=" * 35)
            print("GIT AUTOMATION TOOL")
            print("=" * 35)


        def run_command(self,choice):
            result=subprocess.run(self.commands[choice] ,capture_output=True, text=True)
            if result.returncode == 0:
                print(result.stdout)
            else:
                print(result.stderr)

git=GitAutomation()

while True:
    git.show_header()
    git.show_menu()

                
    try:
        choice=int(input("enter you choice:"))
        if choice == 10:
            print("Good Bye")
            break
        
        elif choice in git.commands:
            
            git.run_command(choice)
        else:
            print("Invalid Choice")

    except ValueError:
         print("invalid value")
         


