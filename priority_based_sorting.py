
#----------------------------------------#
Question: 19
Level: 3

# Question:
# You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
# 1: Sort based on name;
# 2: Then sort based on age;
# 3: Then sort by score.
# The priority is that name > age > score.
# If the following tuples are given as input to the program:
# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
# Then, the output of the program should be:
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

def sorting_priority_wise(req_list):
    sorted_list = sorted(req_list, key=lambda element: (element[0], element[1], element[2]))

    return sorted_list


def main():
    input_params ='''Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85'''

    req_list = []
    for value in input_params.split('\n'):
        print(value)
        name, age, height = value.split(',')
        req_list.append((name, int(age), int(height)))

    sorted_list = sorting_priority_wise(req_list)

    print('Documentation ',abs.__doc__)

    print('Help about function: ', help(abs))

if __name__ == "__main__":
    main()