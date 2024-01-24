from random import randint


def main():
    print("\nWelcome to the Random Name Generator by Thijz!")

    input("Press any key to continue...")

    name_amount = int(input("\nEnter the number of names you want to generate: "))
    names = []

    for x in range(name_amount):
        name = input("Enter a name: ")
        names.append(name)

    random_number = randint(0, len(names) - 1)
    random_name = names[random_number]

    print("\nThe number of the randomly selected name is: " + str(random_number) + "!")
    print("The name that has been randomly selected is: " + random_name + "! Congratulations!")

    input("Press any key to continue...")


if __name__ == "__main__":
    main()
