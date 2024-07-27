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

