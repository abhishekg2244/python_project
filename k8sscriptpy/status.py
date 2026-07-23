import subprocess

result=subprocess.run(["kubectl","get","pod"],capture_output=True,text=True)

# print(result.stdout)  #abhi output string me hi

#list banao
spline=result.stdout.splitlines()
# print(spline)

#ab el ek line ko print kro
health_count = 0
unhealth_count = 0

for line in spline[1:]:
    parts = line.split()
    
    pod_name = parts[0]
    status = parts[2]

    # print(pod_name, status)

    if status == "Running":
        print(f"✅ {pod_name} stauts is {status} is Healthy")
        health_count=health_count+1

    else:
        print(f"❌ {pod_name} stauts is {status} is unHealthy")
        unhealth_count=unhealth_count+1

print(f"healthcount:{health_count}")
print(f"unhealthcount:{unhealth_count}")

 
    



 