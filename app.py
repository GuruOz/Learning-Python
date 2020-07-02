import random
x = 0
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
for x in range(10000000):
    die = random.randint(1, 6)
    if die == 1:
        one += 1
    elif die == 2:
        two += 1
    elif die == 3:
        three+=1
    elif die == 4:
        four+=1
    elif die == 5:
        five+=1
    elif die == 6:
        six+=1

    x+1

print("The number of times one was rolled is: " + str(one))
print("The number of times two was rolled is: " + str(two))
print("The number of times three was rolled is: " + str(three))
print("The number of times four was rolled is: " + str(four))
print("The number of times five was rolled is: " + str(five))
print("The number of times six was rolled is: " + str(six))


