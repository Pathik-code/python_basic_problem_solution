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