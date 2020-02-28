<<<<<<< HEAD

# Programmer: Brendan Loukes
# Date: 12.16.19
# Program: Guess My Number



MyNumber = 7

print("\nGuess a number between 1 & 10\n")

# Ask users to guess
guess = int(input("Enter a Guess: "))

# Keep asking users to guess my number until
# it is equal to MyNumber
while guess != MyNumber:
        print("\nNope, guess again: ")
        guess = int(input("Enter a Guess: "))

print("\nCongratulations, you guessed my number!!!\n")






# Programmer: Brendan Loukes
# Date: 12.19.19
# Program: 1 - 10


x = 1

# While loop will see if a condition has been met
# If not it will run again until the condition
# has been met

while x <= 10:
        print(x)
        x+=1

#Programmer: Brendan Loukes
#Date: 1.6.20
#Program: Running Total, Part II

#This program asks users for five numbers
#It then sums up the numbers


sum = 0
how_many_numbers = int(input("\nHow many numbers would you like to sum up: "))
print("")

for i in range(how_many_numbers):
    enter_a_number = int(input("Enter a number: "))
    sum = sum + enter_a_number

print("\nSum of your numbers is: " + str(sum))


#Programmer: Brendan Loukes
#Date: 1.7.20
#Program: Average Test Scores

#This program asks users how many tests they wish to average


total = 0
how_many_tests = int(input("\nHow many tests would you like to average: "))
print("")

for i in range(how_many_tests):
    enter_a_score = float(input("Enter a score: "))
    total = total + enter_a_score

Average = total / how_many_tests

print("\nAverage: " + str(round(Average, 2)))
=======
# Date 2.3.20

#Programmer: Brenda Loukes

# Declare Global variables here

#name = input("what is your name: ")
x=15


# Create Functions Here

# Greeting Function
def greeting():
    Print("Hi there")
    print("Very nice to meet you"+ name)

# Functions and Local Variables
def printSomethng():
    x=3
    print(x)
# Functions and Parameters
def printNumbers(age); #function name = printNumber with a PARAMETER of age
    print(age)

# Default Parameter values
def printtwonumbers(x,y=71):
    print("First Parameter(Number):"+str(x))
    print("Second Parameter(Number):" + str(x))

#Print Sum
def printSum(x,y):
    print(x + y)
#print multiple terms
def printMultipleTimes(string, times):
    for i in range(times):
        print(string)

# Cal Functions Here
    print("\nGreetings Function\n")
    greeting()

    print("\nPrint Something Funtions\n")
    printSomething()

#print(x)

print("\nPrint number funciton\n")
printnumber(28)
printnumber(38)

print("\nprint two numbers function\n")
printtwonumbers(23,78)

print("\ndefault Patameter Values Function\n")
printtwonumbers(45)
printSum(1,17)

print("\nPrint Multiple Times Function\n")
printMultipletimes("I love Computer Science", 13)

print("\nThanks for hanging out with me through my functions")
>>>>>>> Functions&Paramiters
