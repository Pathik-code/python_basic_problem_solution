#----------------------------------------#
Question: 7
Level: 2

# Question:
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 

class two_d_array():

    def __init__(self):
        self.x = None
        self.y = None
        self.two_d_array = []

    def take_input(self):
        self.x = int(input('Enter Array First Number: '))
        self.y = int(input('Enter Array Second Number: '))
    
    def array_creation(self):
        # Initialize the 2D array with zeros or any default value
        self.two_d_array = [[0 for _ in range(self.y)] for _ in range(self.x)]

        for i in range(self.x):
            for j in range(self.y):
                self.two_d_array[i][j] = j + j * (i - 1)

        print(self.two_d_array)

        


def main():
    y = two_d_array()
    y.take_input()
    y.array_creation()

if __name__ == "__main__":
    main()