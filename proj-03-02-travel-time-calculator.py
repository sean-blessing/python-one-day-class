from math import floor
print("Welcome to the travel time calculator")

choice = "y"
while choice.lower() == "y":
    print()
    miles = float(input("Enter miles:        "))
    mph = float(input("Enter miles per hour:  "))
    print()
    hours_minutes = miles / mph
    #print(f"hours_minutes = {hours_minutes}")
    hours = floor(hours_minutes)
    minutes_float = hours_minutes - hours
    #print(f"minutes_float = {minutes_float}")
    minutes = floor(minutes_float * 60)
    print("Estimated travel time")
    print("=====================")
    print(f"Hours:   {hours}")
    print(f"Minutes: {minutes}")
    print()
    choice = input("Continue? (y/n) ")

print("Bye")