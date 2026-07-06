height = float(input("What is your height?\n"))
weight = float(input("What is your weight?\n"))

bmi = round(weight / (height ** 2), 2)

print("Your BMI is", bmi)
