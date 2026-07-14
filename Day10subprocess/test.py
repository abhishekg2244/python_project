import subprocess

# # Step 1:
# Git version nikalo
version1=subprocess.run(
        ["git","--version"],
        capture_output=True,
        text=True
)

# # Step 2:
# Agar success ho:
#     print("Git Installed")
if version1.returncode == 0:
    print("Git Installed")

# # Step 3:
# Agar fail ho:
#     print("Git Not Installed")
else:
    print("Git Not Installed")
# # Step 4:
# Git version bhi print karo.
print(version1.stdout)