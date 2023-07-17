import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

def choise(name, select):
    if select == 1:
        print(f"{name} have choise {rock}")
    elif select == 2:
        print(f"{name} have choise {paper}")
    else:
        print(f"{name} have choise {scissors}")


print("Welcome to rock-paper-scissors game")

check = False
while check == False:
    select = int(input("Choose one: \n 1. Rock \n 2. Paper \n 3. Scissors \n"))
    if select == 1 or select == 2 or select == 3:
        check = True
    else:
        print("Wrong answer")

select_cpu = int(random.randint(1,3))
print(select_cpu)
choise("You", select)
choise("Cpu", select_cpu)

if select == select_cpu:
    print("Tame!")
elif select == 1 and select_cpu == 2:
    print("You lose!")
elif select == 2 and select_cpu == 3:
    print("You lose!")
elif select == 3 and select_cpu == 1:
    print("You lose!")
else:
    print("You win!!!")
