#ODD OR EVEN
num = int(input("Write a numer: "))

#if num % 2 == 0:
#    print(f"The number {num} is odd")
#else:
#    print(f"The number {num} is even")


#BMI calculator
def bmi(weight, height):
    bmi = round(weight / (height * height),2)
    print(bmi)
    if bmi < 18.5:
        return "Your are underweight"
    elif bmi < 25:
        return "Your have normal weight"
    elif bmi < 35:
        return "Your are obese"
    else:
        return "Your are clinically obese"

#print ("Welcome to BMI Calculator")
#weight = float(input("Which is your weight?: "))
#height = float(input("Which is your height?: "))

#print(bmi(weight,height))

# Leap Year

year = int(input("Write a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"The {year} is a leap year")
        else:
            print(f"The {year} is a NOT leap year")
    else:
        print(f"The {year} is a leap year")
else:
    print(f"The {year} is a NOT leap year")
