name1 = input("Write your name: ").lower()
name2 = input("Write your name: ").lower()

word1 = "true"
word2 = "love"

def count(name,word):
    sum = 0
    for i in word:
        sum = name.count(i) + sum
    return sum

sum1 = count(name1,word1)
sum2 = count(name2,word1)
sum3 = count(name1,word2)
sum4 = count(name2,word2)

sum_T = sum1 + sum2
sum_L = sum3 + sum4
score = int(str(sum_T) + str(sum_L))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together")
else:
    print(f"Your score is {score}")
