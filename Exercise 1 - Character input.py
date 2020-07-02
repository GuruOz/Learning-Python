#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

name = ""
age = 0
currentyear = 2020

print('Enter your name: ')
name = input()
print('Enter your age: ')
age = int(input())
y = int(input("How many times do you want me to print the year?"))
for i in range(y):
    print(name + " you will turn 100 at the year: " + str((100-age)+currentyear))


#things learnt:
#gotta convert the input into an int. Input is taken as string in python. This script also shows the the different ways of asking for input


