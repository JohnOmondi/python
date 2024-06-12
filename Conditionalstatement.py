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

num = int(input("2: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))