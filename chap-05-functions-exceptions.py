print("Welcome to functions and exceptions")

# define a function that adds 2 numbers
# def add_function(num1, num2):
#     return num1 + num2

# print(f"add_function(5,7) = {add_function(5, 7)}")

# default values
# def add_function(num1, num2=2):
#     return num1 + num2

# print(f"add_function(5) = {add_function(5)}")

# Variable arguments
def add_function(*nbrs):
    sum = 0;
    for n in nbrs:
        sum += n
    return sum

print(f"add_function(1,2) = {add_function(1,2)}")
print(f"add_function(2, 4, 6) = {add_function(2, 4, 6)}")
print(f"add_function(1, 3, 5, 7, 9) = {add_function(1, 3, 5, 7, 9)}")

#keyword arguments
# line item (product price, product quantity, handling fee (per line item))
# (price * qty) + handlingFee
def calc_total_function(price, quantity, handling_fee):
    return (price*quantity) + handling_fee

print(calc_total_function(20, 2, 3))
print(calc_total_function(3, 2, 20))
print(calc_total_function(handling_fee=5, quantity=7, price=10))

print("\n ************ Exceptions *************")
def get_whole_number(prompt):
    while True:
        try:
            whole_number = int(input(prompt))
            break
        except ValueError:
            print("Invalid entry. Please try again.")
            
    return whole_number

whole_nbr = get_whole_number("Enter a whole number: ")

print("Bye")