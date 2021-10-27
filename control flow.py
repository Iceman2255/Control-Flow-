# program: Isaac Harlacher-Buckmaster
# Date 10-11-2021
# program: ATM Bank Transaction

"""
This program simulates an ATM utilizing If, Elif, & Else statements
Nesting If statements and refresh our comparison & logical operators
"""

print("Welcome to Cash-R-Us Bank\nLet's take a moment to set up your account.\n")

# Set up account by asking users for their first & last names using Variables
firstName =input("What is your first name: ")
lastName =input ("What is your last name:")

print("\nWelcome to Cash-R-Us",firstName,lastName + ",we will now set up a security PIN on your account.\n")

# set up a PIN - personal Identification number
PIN = input("please choose a 4-digit personal Identification Number: ")

print("\nThank you",firstName + ", we see that you set your pin to",2255)

print("\nWould you like to make a transaction through our Automated Teller Machine")
atm = input("yes or no: ").lower()
if atm == "yes":
    print("\n*******************************************\n")

    # This part of the program will be asking users to complete a transaction  through the ATM
    print("Please insert your ATM card\n")
    print("Welcome to Cash-R-Us ATM",firstName,lastName,"\n")
    userPIN = input("What is your four digit PIN: ")

    if PIN == userPIN:
        balance = 674
        print("\nYour balance: $" + str(balance))



    else:
        print("Sorry",firstName,lastName,"Your PIN doesn't match out records")




else:
    print("\nHave a wonderful day",firstName,lastName + ", please come back and visit us soon,")