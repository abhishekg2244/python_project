servers = ["dev", "qa", "uat", "prod"]

# Write a program that checks:

# Is "qa" present?
for qa in servers:
    print("present")
else:
    print("not present")

# Is "dr" present?
for dr in servers:
    print("present")
else:
    print("not present")

# If "prod" exists, print:
for prod in servers:
    print("exist")
else:
    print("not exist")