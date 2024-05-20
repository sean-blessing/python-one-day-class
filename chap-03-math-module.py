print(f"max and min...")
max_nbr = max(5, 25)
print(f"max_nbr = {max_nbr}")
max_nbr = max(5, 25, 30)
print(f"max_nbr = {max_nbr}")
min_nbr = min(200, 75, 150)
print(f"min_nbr = {min_nbr}")

total = sum([5, 200, 75, 22])
print(f"sum = {total}")

print("\n---------- Rounding -------------")
rounded_nbr = round(9.55782)
print(f"rounded_nbr = {rounded_nbr}")
nbr_1 = 9.55725
# round nbr_1 to 3 decimal places
rounded_nbr = round(nbr_1 * 1000) / 1000
print(f"rounded_nbr = {rounded_nbr}")

print("\n-------- ceil and floor ----------")
#from math import ceil, floor
import math
ceil_nbr = math.ceil(5.5)
floor_nbr = math.floor(5.5)
print(f"ceil_nbr = {ceil_nbr}, floor_nbr = {floor_nbr}")

print("\n---------- random ------")
import random
die_roll = random.randint(1, 6)
print(f"die_roll = {die_roll}")

print("\n------- string formatting ----------")
price = 20000
price_currency = "${:,.2f}".format(price)   #$20,000.00
print(f"price_currency = {price_currency}")
grade = .9995
grade_pct_1 = format(grade, '%')
print(f"grade_pct_1 = {grade_pct_1}")
grade_pct_2 = "{:.2%}".format(grade)        #99.95%
print(f"grade_pct_2 = {grade_pct_2}")
print(f"Format % w/ 2 decimals in string: {grade:.2%}") #99.95%
 