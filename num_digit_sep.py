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