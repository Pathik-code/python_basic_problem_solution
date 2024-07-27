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