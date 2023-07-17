import random
from word_list import word_list
from hangman_art import *

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6


print(f"Testing word: {chosen_word}")

print(logo)

display = []
for i in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()

    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")
    if "_" not in display:
        end_of_game = True
        print ("You win")

    print(f"{''.join(display)}")

    print(stages[lives])
