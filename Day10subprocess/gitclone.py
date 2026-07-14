import subprocess

result=subprocess.run(["git", "clone", "https://github.com/abhishekg2244/TerraformProject.git"])
capture_output=True,
text=True

if result.returncode == 0:
    print("successfull")

else:
    print("not clone")
    print(result.stderr)