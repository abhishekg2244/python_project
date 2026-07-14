tools = ["Git", "Docker", "Kubernetes", "Terraform"]

# "Docker Installed" agar Docker list me ho.
# "Helm Not Installed" agar Helm list me na ho.
# "Terraform Available" agar Terraform ho.

# Rule: Sirf if aur in operator use karna hai. for loop nahi.

if "Docker" in tools:
    print ("Docker Installed" )

if "Helm" in tools:
    print ("helm Installed" )
else:
    print ("Helm Not Installed" )


if "Terraform" in tools:
    print ("Terraform Available" )
else:
    print ("Terraform not Available" )
   
