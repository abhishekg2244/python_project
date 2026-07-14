# ==========================
# Employee Details
# ==========================
# Name       : Abhishek
# Age        : 32
# Team       : DevOps
# Experience : 5 Years
# Location   : Noida
# Salary     : ₹85000
# ==========================

### User Input ######
print("=======================================")
print("Please provide details of employee")
print("=======================================")

name=input("Enter you Name")
age= input(" Enter you Age")
team= input(" Enter you Team")
experience= input(" Enter you experience")
location= input(" Enter you Location")
salary= input(" Enter you Salary")

team_details=f"""
====== Team Details =========

Name : {name}
Age :{age}
Team: {team}
Experience:{experience}
Location:{location}
Salary:{salary}
==============================
"""

print(team_details)
