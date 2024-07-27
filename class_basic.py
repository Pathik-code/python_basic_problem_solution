#----------------------------------------#
# Question: 5
# Level: 1

# Question:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

class class_test():

    def __init__(self):
        self.x = ''
    
    def getstring(self):
        self.x = input('Enter the valid input: ')

    def printstring(self):
        print('Value of intiated variable: ', self.x)


def main():
    y = class_test()
    y.getstring()

    y.printstring()



if __name__ == "__main__":
    main()

