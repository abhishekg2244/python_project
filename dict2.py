student = {
    "Name": "Abhishek",
    "Age": 32,
    "Course": "Python",
    "City": "Noida"
}

print (student)   # print dictionary
print(type(student))  # print type 
print(student.keys())  # print only key
print(student.values()) #print Values only
print(student.items()) # print complete dict

student.update({"wife":"chetana"})
print (student)