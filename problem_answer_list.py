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

####################################################################################################################

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

##################################################################################################################

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

##################################################################################################################
#----------------------------------------#
# Question: 8
# Level: 2

# Question:
# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world

def sorting_words(com_words):
    word_list = com_words.split(',')

    # is the function whichy sort the array and return the new array
    new_word_list = sorted(word_list)

    # in this sort function it sort he current list and return None. If we applied any other feature then it may create the issue
    word_list.sort()

    return new_word_list

def main():
    com_words = input('Enter the Comma Seperated Words: ')

    new = sorting_words(com_words)

    print(','.join(x for x in new))


if __name__ == "__main__":
    main()



##################################################################################################################
#----------------------------------------#
Question: 10
Level: 2

# Question:
# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world




def main():
    sentence = input('Enter the whitespace seperated sentence: ')

    dup_rem = set()

    sen_list = sentence.split(' ')

    for x in sen_list:
        # set has no attribute append , it's has attribute add
        dup_rem.add(x)
    
    # after using the sorted return type is list
    sorted_list = sorted(dup_rem)

    print(' '.join(sorted_list))




if __name__ == "__main__":
    main()

##################################################################################################################
Question: 11
Level: 2

# Question:
# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010


class bin_to_numbers:

    def __init__(self, bin_numbers):
        self.bin_numbers = bin_numbers
        self.dec_number = 0
        self.length = 0
        self.five_div = []

    def number_finding(self):
        for x in self.bin_numbers.split(','):
            self.length = len(x)
            self.dec_number = 0
            for j in x:
                self.dec_number += int(j)*pow(2, self.length -1)
                self.length = self.length - 1
            # print(self.dec_number)
            if self.dec_number % 5 == 0:
                self.five_div.append(x)

        return self.five_div
        

def main():
    bin_numbers = input('Enter the binary numbers in comma sperated: ')
    y = bin_to_numbers(bin_numbers)
    div_number = y.number_finding()
    print(",".join(div_number))
    
if __name__ == "__main__":
    main()
##################################################################################################################
#----------------------------------------#
Question: 12
Level: 2

# Question:
# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.


def main():
    start_number = int(input('Enter the start number: '))
    end_number = int(input('Enter the ending number: '))
    

    odd_list = ['1','3','5','7','9']
    even_digit_number = []
    for i in range(start_number, end_number + 1, 1):
        if any(x in str(i) for x in odd_list):
            pass
        else:
            even_digit_number.append(i)
    print(even_digit_number)


if __name__ == "__main__":
    main()


##################################################################################################################
#----------------------------------------#
Question: 13
Level: 2

# Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3


# to get the ascii value of the any character we use it ord(x)

def num_word(input_str):

    is_numeric = True
    is_word = True

    for char in input_str:
        # Check if the character is a digit (ASCII values for '0' to '9' are 48 to 57)
        if not (48 <= ord(char) <= 57):
            is_numeric = False
        
        # Check if the character is a letter (ASCII values for 'a' to 'z' are 97 to 122 and 'A' to 'Z' are 65 to 90)
        if not ((65 <= ord(char) <= 90) or (97 <= ord(char) <= 122)):
            is_word = False

    return is_numeric, is_word

def main():
    sen = input('Enter the mixed sentence: ')
    words = []
    number = []

    sen_list = sen.split(" ")

    for i in sen_list:
        is_numeric, is_word = num_word(i)
        if is_numeric == False and is_word == True:
            print(f"{i} is a Word")     
        elif is_word == False and is_numeric == True:
            print(f"{i} is a Number")
        else:
            print(f"{i} is a mix words")
        

if __name__ == "__main__":
    main()


##################################################################################################################
#----------------------------------------#
Question: 14
Level: 2

# Question:
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9



def upper_lower_case_finder(input_str):
    upper_count = 0
    lower_count = 0
    # Check if the character is a letter (ASCII values for 'a' to 'z' are 97 to 122 and 'A' to 'Z' are 65 to 90)
    for i in input_str:

        if 97 <= ord(i) <= 122:
            lower_count += 1
        elif 65 <= ord(i) <= 90:
            upper_count += 1
        else:
            print(f'Neither lower or Upper case letter: {i}')
    return upper_count, lower_count

def main():
    
    input_str = input('Enter the Sentence: ')

    upper_count, lower_count = upper_lower_case_finder(input_str)

    print('Upper Case Count: ', {upper_count})
    print('LOwer Case Count: ', {lower_count})


if __name__ == "__main__":
    main()


##################################################################################################################
#----------------------------------------#
Question: 15
Level: 2

# Question:
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106

def getting_addition_output(number_input):
    str_format = 'a+aa+aaa+aaaa'
    str_format = str_format.replace('a','9')
    sum = 0
    for x in str_format.split('+'):
        sum += int(x)
    
    return sum

def main():
    number_input = input('Enter the Number: ')

    sum = getting_addition_output(number_input)

    print(f'Sum of the Number format for {number_input} is:', sum)
if __name__ == "__main__":
    main()


##################################################################################################################

Question: 17
Level: 2

# Question:
# Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
# D 100
# W 200

# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100


def calculate_sum(input_data):
    process, value = input_data.split(" ")

    if process == 'D':
        return +int(value)
    elif process == 'W':
        return -int(value)
    else:
        return

def main():
    sum = 0
    while True:
        input_data = input()

        if input_data.lower() =='done':
            break

        output_num = calculate_sum(input_data)

        sum += output_num
    print('Net Balance: ', sum)

if __name__ == "__main__":
    main()


##################################################################################################################
#----------------------------------------#
Question: 18
Level: 3

# Question:
# A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
# Example
# If the following passwords are given as input to the program:
# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:
# ABd1234@1


def _pass_check(_pass):
    one_lower_case = False
    one_upper_case = False
    one_special_char = False
    one_digit_case = False

    if not (6 <= len(_pass) <= 12):
        return False

    for value in _pass:
        # Check if the character is a letter (ASCII values for 'a' to 'z' are 97 to 122 and 'A' to 'Z' are 65 to 90)
        if 97 <= ord(value) <= 122:
            one_lower_case = True
        elif 65 <= ord(value) <= 90:
            one_upper_case = True
        elif 48 <= ord(value) <= 57:
            one_digit_case = True
        elif value == '@' or value == '#' or value == '$':
            one_special_char = True
        
    return one_upper_case and one_lower_case and one_special_char and one_digit_case
    

        # Check if the character is a digit (ASCII values for '0' to '9' are 48 to 57)

        

def main():
    password_str = input('Enter the comma seperated password: ')
    useful_pass = []
    for _pass in password_str.split(','):
        status = _pass_check(_pass)
        
        if status:
            useful_pass.append(_pass)
    print(','.join(useful_pass))
        
if __name__ == "__main__":
    main()


##################################################################################################################

#----------------------------------------#
Question: 19
Level: 3

# Question:
# You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
# 1: Sort based on name;
# 2: Then sort based on age;
# 3: Then sort by score.
# The priority is that name > age > score.
# If the following tuples are given as input to the program:
# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
# Then, the output of the program should be:
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

def sorting_priority_wise(req_list):
    sorted_list = sorted(req_list, key=lambda element: (element[0], element[1], element[2]))

    return sorted_list


def main():
    input_params ='''Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85'''

    req_list = []
    for value in input_params.split('\n'):
        print(value)
        name, age, height = value.split(',')
        req_list.append((name, int(age), int(height)))

    sorted_list = sorting_priority_wise(req_list)

    print(sorted_list)

if __name__ == "__main__":
    main()


##################################################################################################################

#----------------------------------------#
Question: 22
Level: 3

# Question:
# Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 
# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# Then, the output should be:
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1


def feq_finder(input_str):
    freq_dict = {}
    sorted_list = sorted(input_str.split(" "))
    for value in sorted_list:
        freq_dict[value] = input_str.count(value)

    return freq_dict

def main():
    input_str = input()

    freq_dict = feq_finder(input_str)

    print(freq_dict)


if __name__ == "__main__":
    main()


##################################################################################################################
#----------------------------------------#
Question: 25
Level: 1

# Question:
#     Define a class, which have a class parameter and have a same instance parameter.

class Person():

    name = "Saurav"

    def __init__(self, name):
        self.name = name


def main():

    x = Person("Pathik")

    print(f"Class params:", Person.name)
    print(f"Instance variable:", x.name)

if __name__ == "__main__":
    main()


##################################################################################################################



##################################################################################################################



##################################################################################################################



##################################################################################################################


##################################################################################################################

