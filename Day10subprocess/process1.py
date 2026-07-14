import subprocess

result = subprocess.run(
    ["git", "abc"],
    capture_output=True,
    text=True
)

print(type(result))
print(result.stdout)
print(result.stderr)
print(result.returncode)