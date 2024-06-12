
courses = ["MIT", "Cybersecurity", "Datascience"]
print(courses)
#accessing an element in an array

print(courses[0])

#Adding a new element in array
courses.append("Adroid development")
print(courses)

#deleting an element in an array
courses.remove("Cybersecurity")
print(courses)

#looping through an array

for course in courses:
    print(course)

