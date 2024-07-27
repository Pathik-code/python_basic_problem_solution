

# Please write a program which prints all permutations of [1,2,3]


# Hints:
# Use itertools.permutations() to get permutations of list.



import itertools
print(list(itertools.permutations([1,2,3])))





# Question:

# Write a program to solve a classic ancient Chinese puzzle: 
# We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?

def main():

    total_heads = 34
    total_legs = 94
    dict = {}
    for i in range(total_heads+1):
        # print(i)
        no_chickens = i
        no_rabbit = total_heads - i

        if (2*no_chickens + 4*no_rabbit) == total_legs:
            dict['Number of chickens'] = no_chickens
            dict['Number of rabbits'] = no_rabbit
            break

    print(dict)

if __name__ == "__main__":
    main()


