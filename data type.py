#data type



number = 60  # Int
num = 45.66  # float
greeting = "Hello there "  # str
isPythonInteresting = True  # boolean
fruits = ["apple", "banana", "cherry"]  # list
cars = ("bmw", "toyota", "v8") #tuple
countries = { "Kenya", "India", "Australia" }
student ={
    "firstname": "John",
    "age" : 19,
    "course" :"MIT",
    "nationality" : "Kenyan"
}  # this is a dictionary

print(num)
print(isPythonInteresting)
print(fruits)
print(cars)
print(countries)
print(student["firstname"])
print(student["age"])
print(student["course"])
print(student["nationality"])


#how to determine data type
print(type(isPythonInteresting))
print(type(cars))




#typecasting is converting one data type to another
print(int(num))
print(float(number))


