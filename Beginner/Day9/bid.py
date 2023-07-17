

bid = {}
def new_bid (nparticipant, nbid):
    nbid[nparticipant[0]] = nparticipant[1]
    return nbid

def new_auction ():
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    new_participant = [name,bid]
    return new_participant

def calc (bid):
    value = 0
    for i in bid:
        value1 = bid[i]
        if value1 > value:
            value = value1
        else:
            pass
    return [i,value]


print("Welcome to the secret auction program.")

cont = True
while cont:
    participant = new_auction()
    bid = new_bid(participant, bid)
    continuar = input("Are there any other bidders? Type 'y' or 'n'").lower()
    if continuar == 'y':
        pass
    else:
        break
winner = calc(bid)
print(f"The winner of the secret auction program is {winner[0]} with a bid of {winner[1]}")
