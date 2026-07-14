Name= "abhishek"
age=32
team= "devops"

Team_Details= print("Name: {}, Age: {}, Team: {}".format(Name, age, team))
Team_Details = print ("Name:", Name , "Age:", age , "team:",team)

# with f string


team_detail_f = f"Name: {Name}, age: {age}, team: {team}"
team_detail_f = f"Name: {Name}, Age: {age}, Team: {team}"
print (team_detail_f)

## f string with multiline

team_details_multiline = f"""
Name : {Name}
Age  : {age}
Team : {team}

"""

print(team_details_multiline)