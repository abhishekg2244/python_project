import subprocess  # execute command

applist=[
    ["git","--version"],
    ["docker","--version"],
    ["aws"],
    ["java" ,"--version"],
    ["python","--version"]
]

print("*" * 35)
print("Application Status")
print("*" * 35)

## Loop for iteration

for toolcheck in applist:

    result=subprocess.run(toolcheck ,capture_output=True ,text=True)

    if result.returncode == 0:
       print("==" * 20)
    #    print(f"{toolcheck}")
       print(f"{toolcheck[0]} is installed")
       print(result.stdout.strip())
    else:
        print(f"{toolcheck[0]} is not installed")
        print(result.stderr.strip())


