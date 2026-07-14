import subprocess

def git_app(command):

    status=subprocess.run(command ,capture_output=True, text=True)
    if status.returncode == 0:
        print("*" * 20)
        print(status.stdout)
    else:
        print("*" * 20)
        print(status.stderr)


git_app(["git","status"])
