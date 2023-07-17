import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def random_card(cards):
    i = random.randint(0,len(cards)-1)
    r_card = cards[i]
    return r_card

def give_card(user):
    card = random_card(cards)
    user.append(card)
    return user

def add_card(user,total_hand = 0):
    for i in user:
        total_hand = i + total_hand
    return total_hand

def check_hand(user):
    total_hand = add_card(user)
    if total_hand > 21:
        return True
    else:
        return False

game = 'y'

while game == 'y':
    game = input("Do you want play Black Jack?: y/n: ").lower()
    human_hand = []
    ia_hand = []
    #Primera ronda
    #Reparte 2 a humano y 2 a IA
    for i in range(0,2):
        human_hand = give_card(human_hand)
        ia_hand = give_card(ia_hand)
    print(f"{human_hand} -> {add_card(human_hand)}")
    print(ia_hand)

    new_card = 'y'
    while new_card == 'y':
        new_card = input("Do you want a new card?: y/n ").lower()
        if new_card == 'y':
            human_hand = give_card(human_hand)
            print(f"{human_hand} -> {add_card(human_hand)}")
            if check_hand(human_hand) == True:
                print("You loose :(")
                break
            else:
                pass
        else:
            while add_card(ia_hand) <= 21:
                if add_card(ia_hand) > add_card(human_hand) and add_card(ia_hand) <= 21:
                    print("You loose :(")
                    break
                ia_hand = give_card(ia_hand)
                print(f'{ia_hand} -> {add_card(ia_hand)}')
                input("Pulse para continuar)...")
                if add_card(ia_hand) > 21:
                    print("You win!!!")

print("Thanks you for play Black Jack")
