import subprocess


class AutomationTool:
    def run_command(self, command):
        result = subprocess.run(command, capture_output=True, text=True)

        if result.returncode == 0:
            print(result.stdout)
        else:
            print(result.stderr)

    def show_header(self, title):
        print("=" * 40)
        print(title)
        print("=" * 40)


class GitAutomation(AutomationTool):
    def __init__(self):
        self.commands = {
            1: ["git", "--version"],
            2: ["git", "status"],
            3: ["git", "branch"],
            4: ["git", "log", "--oneline"],
            5: ["git", "remote", "-v"],
            6: ["git", "pull"],
            7: ["git", "push"],
            8: ["git", "add", "."]
        }

    def show_menu(self):
        print("\n------ GIT MENU ------")
        print("1. Git Version")
        print("2. Git Status")
        print("3. Git Branch")
        print("4. Git Log")
        print("5. Git Remote")
        print("6. Git Pull")
        print("7. Git Push")
        print("8. Git Add .")
        print("9. Back")


class DockerAutomation(AutomationTool):
    def __init__(self):
        self.commands = {
            1: ["docker", "--version"],
            2: ["docker", "info"],
            3: ["docker", "images"],
            4: ["docker", "container", "ls"],
            5: ["docker", "ps"]
        }

    def show_menu(self):
        print("\n------ DOCKER MENU ------")
        print("1. Docker Version")
        print("2. Docker Info")
        print("3. Docker Images")
        print("4. Docker Container List")
        print("5. Docker PS")
        print("6. Back")


class DevOpsToolkit:
    def __init__(self):
        self.git = GitAutomation()
        self.docker = DockerAutomation()

    def show_main_menu(self):
        print("\n")
        print("=" * 40)
        print("      DEVOPS TOOLKIT")
        print("=" * 40)
        print("1. Git")
        print("2. Docker")
        print("3. Exit")

    def run_git(self):
        while True:
            self.git.show_header("GIT AUTOMATION")
            self.git.show_menu()

            try:
                choice = int(input("Enter choice: "))

                if choice == 9:
                    break

                elif choice in self.git.commands:
                    self.git.run_command(self.git.commands[choice])

                else:
                    print("Invalid Choice")

            except ValueError:
                print("Please enter a valid number.")

    def run_docker(self):
        while True:
            self.docker.show_header("DOCKER AUTOMATION")
            self.docker.show_menu()

            try:
                choice = int(input("Enter choice: "))

                if choice == 6:
                    break

                elif choice in self.docker.commands:
                    self.docker.run_c2ommand(self.docker.commands[choice])

                else:
                    print("Invalid Choice")

            except ValueError:
                print("Please enter a valid number.")

    def start(self):
        while True:
            self.show_main_menu()

            try:
                choice = int(input("Select Tool: "))

                if choice == 1:
                    self.run_git()

                elif choice == 2:
                    self.run_docker()

                elif choice == 3:
                    print("Good Bye!")
                    break

                else:
                    print("Invalid Choice")

            except ValueError:
                print("Please enter a valid number.")


toolkit = DevOpsToolkit()
toolkit.start()