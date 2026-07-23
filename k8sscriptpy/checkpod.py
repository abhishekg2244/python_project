import subprocess

result=subprocess.run(["kubectl", "get", "ns"],capture_output=True, text=True)
# print(result)
print(type(result))

# print(result.stdout)

lines = result.stdout.splitlines()
# print(lines)
print(type(lines))

# for line in lines:
#     print(line.splitlines())
#     # print(type(line))
for line in lines[1:]:
    parts = line.split()
    # print(parts)
    print(parts[0])   # Namespace
    print(parts[1])   # Status
    print(parts[2]) 
    