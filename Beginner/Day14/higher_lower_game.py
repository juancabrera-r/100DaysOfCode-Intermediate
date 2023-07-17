import random
from game_data import data


# Random number
def random_number():
    # n = random.randint(0,len(data)-1)
    # data_list = data[n]
    data_list = random.choice(data)
    return data_list


def compare(opt_A, opt_B):
    print(f"Compare A: {opt_A['name']}, a {opt_A['description']}, from {opt_A['country']}")
    print(f"Compare B: {opt_B['name']}, a {opt_B['description']}, from {opt_B['country']}")
    followers_A = opt_A['follower_count']
    followers_B = opt_B['follower_count']
    if followers_A > followers_B:
        return 'a'
    else:
        return 'b'


game_over = False
while not game_over:
    option_A = random_number()
    option_B = random_number()

    solution = compare(option_A, option_B)

    attempt = False
    while not attempt:
        answare = input("Who has more followers? 'A' or 'B': ").lower()
        if solution == answare:
            option_A = option_B
            option_B = random_number()
            solution = compare(option_A, option_B)
        else:
            print("You have fail!")
            game_over = True
            attempt = True
