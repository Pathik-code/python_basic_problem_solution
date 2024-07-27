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