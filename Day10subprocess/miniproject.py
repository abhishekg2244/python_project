# =========================
# DevOps Tool Health Check
# =========================

# Checking git...
# ✅ Git Installed

# Checking docker...
# ✅ Docker Installed

# Checking terraform...
# ✅ Terraform Installed

# Checking kubectl...
# ❌ Kubectl Not Installed

import subprocess

git_status=subprocess.run(["git" ,"--version"], capture_output=True,text=True)


if git_status.returncode == 0:
    print("git installed")
    print(git_status.stdout)

terraform_status=subprocess.run(["terraform" ,"--version"], capture_output=True,text=True)
if terraform_status.returncode == 0:
    print("terraform installed") 
    print(terraform_status.stdout)

docker_status=subprocess.run(["docker" ,"--version"], capture_output=True,text=True)
if docker_status.returncode == 0:
    print("Docker installed") 
    print(docker_status.stdout)
else:
    print("not installed")

kubectl_status=subprocess.run(["kubectl" ,"get","ns"], capture_output=True,text=True)
if kubectl_status.returncode == 0:
    print("Kubectl installed") 
    print(kubectl_status.stdout)
else:
    print("not installed")