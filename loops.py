#while loop
#increment
number = 20
while number <= 25:
    print(number)
    number += 1

num = 105
while num >= 110:
    print(num)
    num += 1

#decrement
count = 10
while count >= 1:
    print(count)
    count -= 1

#break and continue statement
x = 25
while x <= 30:
    print(x)
    if x == 27:
        break
    x +=  1


y = 0
while y <= 5:
    y += 1
    if y == 3:
        continue
    print(y)
#for loop

for b in range(7):
    print(b)

for z in range(40, 45):
    print(z)

for mynumber in range(100,110,3):
    print(mynumber)


languages = ["Kotlin", "python", "javascript", "PHP"]
for lang in languages:
    print(lang)