#----------------------------------------#
Question: 25
Level: 1

# Question:
#     Define a class, which have a class parameter and have a same instance parameter.

class Person():

    name = "Saurav"

    def __init__(self, name):
        self.name = name


def main():

    x = Person("Pathik")

    print(f"Class params:", Person.name)
    print(f"Instance variable:", x.name)

if __name__ == "__main__":
    main()