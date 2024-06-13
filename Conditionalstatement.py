temperature = 32
if temperature < 25:
    print("It is cold")
elif temperature > 25:
    print("It is hot")
else:
    print("Normal temperature")

#A program that returns the largest number among three numbers

first = 56
second = 23
third = 78

if first > second and first > third:
    print(first, "is the largest number")

elif second >first and second > third:
    print(second,"is the largest number")
else:
    print(third,"is the largest number")

#a python program that checks whether a number is even or odd

number = 3
if number  == 0:
    print(number, "is neutral")
elif number % 2 == 0:
    print(number,"even")
else:
    print( number, " is odd")

#a python program that returns the area of a rectangle
#a = l*w
length= 20
width= 5
area = length*width
print(area)

#a python program that returns the area of a trapizium
# area= 1/2 (a+b)h

a = 15
b = 20
h = 12
area = 1/2 * (a + b) * h
print(area)