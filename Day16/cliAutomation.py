import subprocess

class AutomationTool:
    def run_command(self, choice):
        result = subprocess.run(
            self.commands[choice],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            print(result.stdout)
        else:
            print(result.stderr)

    def show_header(self, title):
        print("=" * 35)
        print(title)
        print("=" * 35)


class gitAutomation(AutomationTool):
    # git.show_header("GIT AUTOMATION TOOL")
    def __init__(self):
        self.commands = {
            1: ["git", "--version"],
            2: ["git", "status"],
            3: ["git", "branch"],
            4: ["git", "log", "--oneline"],
            5: ["git", "remote", "-v"],
            6: ["git", "pull"],
            7: ["git", "push"],
            8: ["git", "add", "."],
            # 9 :["git","commit","-m","putmsg"],
            9: ["exit"]
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



class dockerAutomation(AutomationTool):
    # docker.show_header("DOCKER AUTOMATION TOOL")
    def  __init__(self):
        self.commands = {
            1: ["docker", "version"],
            2: ["docker", "info"],
            3: ["docker", "images"],
            4: ["docker", "containers", "ls"],
            5: ["docker", "ps"],
            6: ["docker", "build", "-t", "myapp", "."],
            7: ["docker", "run", "-d", "-p", "8080:8080", "myapp"],
            8: ["docker", "stop", "<container_id>"],
            9: ["docker", "rm", "<container_id>"],
            10: ["exit"]
        }
    def show_menu(self):
        print("1 : docker version")
        print("2 : docker info")
        print("3 : docker images")
        print("4 : docker containers ls")
        print("5 : docker ps")
        print("6 : docker build -t myapp .")
        print("7 : docker run -d -p 8080:8080 myapp")
        print("8 : docker stop <container_id>")
        print("9 : docker rm <container_id>")
        print("10: Exit")


class  DevOpsToolkit():
     def __init__(self):

        self.docker=dockerAutomation()
        self.git=gitAutomation()
        
        print("=="*10)
        print("select devops Tool kit")
        print("Select 1 for Git")
        print("select 2 for Docker")
        print("=="*10)
        try:
            choose=int(input("choose 1 for git and 2 for docker: "))

            if choose==1:
                self.git.show_header("Git Automation tool")
                self.git.show_menu()
                self.git.run_command(int(input("choose your option: ")))
            elif choose ==2:
                self.docker.show_header("Docker Automation Tool")
                self.docker.show_menu()
                self.docker.run_command(int(input("choose your option: ")))
            else:
                print("choose valid number")
        except ValueError:
            print("choose numner only")


toolkit=DevOpsToolkit()




