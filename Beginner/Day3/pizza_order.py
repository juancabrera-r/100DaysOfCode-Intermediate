print("Welcome to pizza order: ")

size = input("Which size of pizza you want?: (L, M, S) ").upper()

if size == "L":
    price = 25
elif size == "M":
    price = 20
else:
    price = 15

if size == "L" or size == "M":
    extra1 = input ("Do you want pepperoni for the pizza?: (Y/N)").upper()
    if extra1 == "Y":
        price = price + 3
else:
    extra1 = input ("Do you want pepperoni for the pizza?: (Y/N)").upper()
    if extra1 == "Y":
        price = price + 2

extra2 = input ("Do you want extra cheese? (Y/N) ")
if extra2 == "Y":
    price = price + 1


print(f"The bill is ${price}")
