#----------------------------------------#
Question: 18
Level: 3

# Question:
# A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
# Example
# If the following passwords are given as input to the program:
# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:
# ABd1234@1


def _pass_check(_pass):
    one_lower_case = False
    one_upper_case = False
    one_special_char = False
    one_digit_case = False

    if not (6 <= len(_pass) <= 12):
        return False

    for value in _pass:
        # Check if the character is a letter (ASCII values for 'a' to 'z' are 97 to 122 and 'A' to 'Z' are 65 to 90)
        if 97 <= ord(value) <= 122:
            one_lower_case = True
        elif 65 <= ord(value) <= 90:
            one_upper_case = True
        elif 48 <= ord(value) <= 57:
            one_digit_case = True
        elif value == '@' or value == '#' or value == '$':
            one_special_char = True
        
    return one_upper_case and one_lower_case and one_special_char and one_digit_case
    

        # Check if the character is a digit (ASCII values for '0' to '9' are 48 to 57)

        

def main():
    password_str = input('Enter the comma seperated password: ')
    useful_pass = []
    for _pass in password_str.split(','):
        status = _pass_check(_pass)
        
        if status:
            useful_pass.append(_pass)
    print(','.join(useful_pass))
        
if __name__ == "__main__":
    main()