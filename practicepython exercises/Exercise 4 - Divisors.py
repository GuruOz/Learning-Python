# Exercise 4 (and Solution)
# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# (If you don’t know what a divisor is, it is a number that divides evenly into another number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

x = int(input("Enter a number: "))
y = x
z = 1
b = []
for z in range(1, x):
    if x % z == 0:
        b.insert(0, z)
print(b)


