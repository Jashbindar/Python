print("Welcome to calculator")

# Addition function
def add(num1, num2):
    return num1 + num2

# Subtraction function
def subtract(num1, num2):
    return num1 - num2

# Division function
def divide(num1, num2):
    return num1 / num2

# Multiplication function
def multiply(num1, num2):
    return num1 + num2

def calculator():
    # will keep looping until operation "5."" is placed
    while True:
        try:
            print("Choose your operation \n1. Addition \n2. Subtraction \n3. Division \n4. Multiplication \n5. End program")
            choice = int(input("\nChoose operation: "))
            while choice not in [1, 2, 3, 4, 5]:
                # if values other than 1, 2, 3, 4, 5 are placed
                print("Invalid choice. Please choose a valid operation")
                choice = int(input("\nChoose operation: "))

            # will stop executing the program
            if (choice == 5):
                print("Exiting program")
                exit()

            # global is used so the parameters can be used in the other function
            global num1, num2
            num1 = eval(input("Number 1: "))
            num2 = eval(input("Number 2: "))

            if (choice == 1):
                print("Answer:", add(num1, num2))
                print()
            elif (choice == 2):
                print("Answer:", subtract(num1, num2))
                print()
            elif (choice == 3):
                while (num2 == 0):
                    # error if num2 = 0
                    print("Error: Division by zero is not allowed")
                    # ask the user to input the right value
                    num2 = eval(input("Number 2: "))
                print("Answer:", divide(num1, num2))
                print()
            else:
                print("Answer:", multiply(num1, num2))
                print()

        except ValueError:
            print("\nPlease enter a numerical character")

# calls the calculator function
calculator()