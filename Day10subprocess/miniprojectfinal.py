import subprocess

tools = [
    ["git", "--version"],
    ["docker", "--version"],
    ["terraform", "--version"]
]

print("=" * 35)
print("DevOps Tool Health Check")
print("=" * 35)

for tool in tools:

    print(f"\nChecking {tool[0]}...")

    result = subprocess.run(tool,capture_output=True,text=True)

    if result.returncode == 0:
        print(f"✅ {tool[0]} Installed")
        print(result.stdout.strip())
    else:
        print(f"❌ {tool[0]} Not Installed")
        print(result.stderr.strip())