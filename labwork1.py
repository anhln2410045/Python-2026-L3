# -*- coding: utf-8 -*-
"""ex1"""

radius = float(input("Enter circle radius? "))
area = 3.14 * (radius ** 2)
print("Circle area =", area)

"""ex2"""

celsius = float(input("Enter temperature in Celsius? "))
fahrenheit = (celsius * 1.8) + 32
print("Temperature in Fahrenheit =", fahrenheit)

"""ex3"""

number = int(input("Enter a number? "))
if number > 1:
    prime = True
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            prime = False
            break
    if prime:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is a NOT prime number")
else:
    print(f"{number} is a NOT prime number")

"""ex4"""

number = int(input("Enter a number? "))
sum = 0
for i in range(1, number):
    if number % i == 0:
        sum += i
if sum == number and number > 0:
    print(f"{number} is a perfect number")
else:
    print(f"{number} is a NOT perfect number")

"""ex5"""

color = ["Blue", "Yellow", "Purple", "Red", "Black"]
favorite_color = input("What is your favorite color? ")
if favorite_color in color:
    index = color.index(favorite_color)
    print(f"Your color is at index {index} in my list")
else:
    print("Sorry, I could not find your color")

"""ex6"""

range1 = list(range(0, 7))
print("range1:", *range1)
range2 = list(range(1, 11, 3))
print("range2:", *range2)
range3 = list(range(5, 0, -1))
print("range3:", *range3)
range4 = list(range(6, -3, -2))
print("range4:", *range4)

"""ex7"""

def remove_dollar_sign(s):
    return s.replace("$", "")
string = input("The string with $: ")
print("New string:", remove_dollar_sign(string))