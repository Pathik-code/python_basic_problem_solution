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