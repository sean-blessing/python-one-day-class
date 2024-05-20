print("Welcome to the factorial calculator")

choice = "y"
while choice.lower() == "y":
    nbr = int(input("\nEnter an integer that's greater than 0 and less than 10: "))
    factorial = 1
    for i in range(1, nbr+1):
        factorial = factorial * i
    print(f"The factorial of {nbr} is {factorial}.")
    choice = input("\nContinue? (y/n): ")

print("bye")