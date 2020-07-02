"""""
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""""

num = int(input("Enter  a number: "))
check = int(input("Enter a number to divide it by: "))
x = 0

if num % check == 0:
    x = num / check
    if x % 2 == 0:
        if x % 4 == 0:
            print("Your number is a multiple of 4!")
            print(x)
        else:
            print("You have entered an even number!")
            print(x)
    else:
        print("Your number is odd!")
        print(x)
else:
    x = num / check
    print("your number does not divide evenly")
    print(x)