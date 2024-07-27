
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