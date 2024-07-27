
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