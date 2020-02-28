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
