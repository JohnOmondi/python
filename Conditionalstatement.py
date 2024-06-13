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
if number % 2 == 0:
    print("even")
else:
    print("odd")