import random

word_list = ["ardark", "baboom", "camel"]

# def random_word (list):
#     word = word_list[int(random.randint(0,len(list)-1))]
#     return word

def create_word(word, guess = []):
    for letter_word in word:
        # guess.append("_")
        guess += "_"
    return guess

def check_letter(letter, word, guess):
    i = 0
    for letter_word in word:
        if letter == letter_word and guess[i] == '_':
            guess[i] =f"{letter}"
        else:
            pass
        i += 1
    return guess

# word = random_word(word_list)
word = random.choice(word_list)
print (word)

game = True
guess = create_word(word)
print(guess)
i = 4

while game:
    letter = input("Write a letter: ").lower()
    guess = check_letter(letter, word, guess)
    print (guess)
    final_word = ''.join(guess)
    print (final_word)
    if final_word == word:
        game = False
        print ("You have win!!!")
    elif i == 0:
        game = False
        print ("You have lose! :(")
    else:
        i -= 1
