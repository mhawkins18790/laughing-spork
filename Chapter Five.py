requested_toppings = ['mushrooms', 'onions', 'pineapple']
print(('mushrooms' in requested_toppings))

single_digits = [value for value in range(1, 10)]


for digits in single_digits:
    if digits == 1:
        print(str(digits) + "st")
    elif digits == 2:
        print(str(digits) + "nd")
    elif digits == 3:
        print(str(digits) + "rd")
    else:
        print(str(digits) + "th")
