import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generator(input1,input2):
    key = []
    for i in range(0,input1):
        let = input2[random.randint(0,len(input2)-1)]
        if random.randint(0,1) == 0:
            key.append(let.upper())
        else:
            key.append(let.lower())
    return key

def insert_random(input1, input2):
    for n in input1:
        ran = random.randint(0,len(input2)-1)
        password.insert(ran, n)
    return password

print ("Welcome to KEY GENERATOR")

letter = int(input("How many letter?: "))
number = int(input("How many number?: "))
symbol = int(input("How many symbols?: "))


letter = (generator(letter,letters))
number = (generator(number,numbers))
symbols = (generator(symbol,symbols))

password2 = letter + number + symbols
random.shuffle(password2)
password2 = ''.join(password2)
print(password2)

password = letter

password = insert_random(number,letter)
password = insert_random(symbols,password)

password = ''.join(password)


print(f"Your new password is: {password}")
