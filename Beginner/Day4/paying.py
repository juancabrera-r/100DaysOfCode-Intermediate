import random

list = "Angela, Ben, Jenny, Michael, Chloe"

list_name = list.split(", ")

print (list_name)

len = len(list_name)
print(len)

person = list_name[random.randint(0,len-1)]

print(f"The person who must pay the bill is {person}")
