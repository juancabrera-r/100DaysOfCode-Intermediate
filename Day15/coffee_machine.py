from menu import MENU

# Ingredients and cost

machine = {'water': 500, 'milk': 500, 'coffee': 500, 'profit': 20.0}


def menu_ingredients(coffee_type):
    ingredients = MENU[coffee_type]["ingredients"]
    return ingredients


def coin_total(quar, dim, nick, penni):
    total = quar*0.25 + dim*0.1 + nick*0.05 + penni*0.01
    return total


def check_money(total, menu_cost):
   change = total - menu_cost
   return change



def check_ingredients(coffee_type):
    ingredients = MENU[coffee_type]["ingredients"]
    coffee_water = ingredients['water']
    if coffee_type == 'latte' or coffee_type == 'cappuccino':
         coffee_milk = ingredients['milk']
    else:
         coffee_milk = 0
    coffee_coffee = ingredients['coffee']

    if machine['water'] >= coffee_water:
        if machine['milk'] >= coffee_milk:
            if machine['coffee'] >= coffee_coffee:
                return True
            else:
                return "Sorry. Not enough coffee"
        else:
            return "Sorry. Not enough milk"
    else:
        return "Sorry. Not enough water"


def check_machine(coffee_type, change):
    machine['water'] = machine['water'] - MENU[coffee_type]["ingredients"]["water"]
    if coffee_type == 'latte' or coffee_type == 'cappuccino':
        machine['milk'] = machine['milk'] - MENU[coffee_type]["ingredients"]["milk"]
    else:
        pass
    machine['coffee'] = machine['coffee'] - MENU[coffee_type]["ingredients"]["coffee"]
    machine['profit'] = machine['profit'] + MENU[coffee_type]["cost"] - change
    return(machine)

machine_working = True
while machine_working:
    # Anyone situation
    menu_order = True

    while menu_order:
        order = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if order == "espresso" or order == "latte" or order == "cappuccino" or order == "report" or order == "off":
            menu_order = False
        else:
            print("Error menu selection")
            pass

    # Maintainers situation
    if order == "report":
        print(machine)
    elif order == "off":
        machine_working = False
        print("The system is clossing...")
    else:

        # User situation

        menu_change = True
        while menu_change:
            quarters = int(input("How many quarters ($0,25): "))
            dimes = int(input("How many dimes ($0,10): "))
            nickles = int(input("How many nickel ($0,05): "))
            pennies = int(input("How many pennies ($0,01): "))
            coins = coin_total(quarters, dimes, nickles, pennies)
            print(f"You have inserted ${coins}")
            if coins >= machine['profit']:
                print("Sorry, we don't have enough change.")
            if coins < MENU[order]["cost"]:
                print("Sorry, not enough money")
            else:
                menu_change = False


        # Make coffee
        if check_ingredients(order) == True:
            print(f"Here is your {order}. Enjoy!")
            change = (check_money(coins, MENU[order]["cost"]))
            print(f"Here your change: ${change}")
        else:
            print(check_ingredients(order))
            print("See you soon")
