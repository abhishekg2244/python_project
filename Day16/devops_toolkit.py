
import subprocess

class DockerAutomation:
    def __init__(self):
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
        print("6 : docker build")
        print("7 : docker run")
        print("8 : docker stop")
        print("9 : docker rm")
        print("10: Exit")

    def show_header(self):
        print("=" * 35)
        print("DOCKER AUTOMATION TOOL")
        print("=" * 35)

    def run_command(self, choice):
        result = subprocess.run(self.commands[choice], capture_output=True, text=True)
        if result.returncode == 0:
            print(result.stdout)
        else:
            print(result.stderr)

docker=DockerAutomation()

while True:
    docker.show_header()
    docker.show_menu()

    try:
        choice=int(input("enter your choice: "))
        if choice == 10:
            print("exit good bye")
            break
        elif  choice in docker.commands.keys():
            print (f" select choice {choice}")
            docker.run_command(choice)
        
        else:
            print ("select correct choice")
 
    except ValueError:
        print ("invalid choice")
        

