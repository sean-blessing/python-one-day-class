print("Welcome to the rectangle calculator!\n")

choice = "y"

while choice == "y" or choice == "Y":
    length = float(input("Enter length: "))
    width = float(input("Enter width:  "))
    area = length * width
    perimeter = 2 * length + 2 * width
    print(f"area:      {area}")
    print(f"perimeter: {perimeter}")

    choice = input("Continue (y/n): ")
    print()
print("Bye")