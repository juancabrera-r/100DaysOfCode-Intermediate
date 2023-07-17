import random

EASY_LEVEL = 10
HARD_LEVEL = 5

def level():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == 'easy':
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def choice_number():
    guess = int(input("Make a guess: "))
    return guess

def check_number(number, random):
    """checking number with random"""
    if number == random:
        return "You had guessed!!!"
    elif number > random and number - random > 10:
        return "Too high"
    elif number < random and random - number > 10:
        return "Too low"
    elif number > random and number - random < 10:
        return "High"
    elif number < random and random - number < 10:
        return "Low"
    else:
        pass

print("Welcom to the Number Guessing Game!")
print("I'm thinking in a number between 1 and 100")

def game():
    attempt = level()

    # random_number = random.choice(range(1,100,1))
    random_number = random.randint(1,100)
    # print(random_number)
    game_over = False

    while not game_over:
        print(f"You have {attempt} attempts remaining to guess the number.")
        guess_number = choice_number()
        print(check_number(guess_number, random_number))
        attempt -= 1
        if attempt == 0:
            print("You don't have more attempts")
            game_over = True
        elif guess_number == random_number:
            game_over = True

game()
