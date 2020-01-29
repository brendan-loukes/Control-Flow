
# Programmer: Brendan Loukes
# Date 1.20.20
# Program: Double For Loop

for i in range(3):
    print("outer for loop " + str(i))
    for k in range(4):
        print("\tinner for loop " + str(k))



print("\n***************\n")

"""
Programmer: Brendan Loukes
Date: 1.23.20
Program: While Loop nested inside of a For Loop
"""

for i in range(4):
    print("for loop" + str(i))
    x = i
    while x >= 0:
        print("\tWhile Loop: " + str(x))
         x = x - 1