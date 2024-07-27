#----------------------------------------#
Question: 6
Level: 2

# Question:
# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24

import math

class formula_calculate():
    

    def __init__(self):
        self.C = 50
        self.H = 30
        self.D = ''
        self.x = None
        self.result = []

    def getString(self):
        self.D = input('Enter the NUmber String With comma seperated: ')

    def calculate_formula(self):
        for i in self.D.split(','):
            self.x = math.sqrt((2*self.C*int(i))/self.H) 
            self.result.append(self.x) 
        return self.result         




def main():
    y = formula_calculate()
    y.getString()
    output = y.calculate_formula()
    v = ','.join(str(int(x)) for x in output)
    print(v)


if __name__ == "__main__":
    main()

