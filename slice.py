# name = "Abhishek"

# Print karo:

# Abhi
# shek
# his

name="Abhishek"
print(name[0:4])
print(name[4:])
print(name[2:5])


bhanji="vanaya"
print(bhanji.upper())

print(bhanji.capitalize())

print(bhanji.title())


test= "Azure devops "
print(test.replace("Azure", "Github"))

image_tag= "frontend:v1.0.0"
print(image_tag.replace("v1.0.0", "v1.0.1"))

tool_stack="CI/CD, DevOps, Azure, Github"
print(tool_stack.split(","))

# #===========================
# Original text
# strip() ka output
# upper()
# lower()
# replace("Terraform", "Ansible")
# split()
text = "  Docker Kubernetes Terraform  "
print(text)
print(text.strip())
print(text.upper())
print(text.lower())
print(text.replace("Terraform","Ansible"))
print(text.split())
