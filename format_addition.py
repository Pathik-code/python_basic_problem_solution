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