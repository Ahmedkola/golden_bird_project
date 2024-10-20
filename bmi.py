print("BMI CALCULATOR")
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
bmi = round(weight / (height ** 2), 2)

if bmi <= 18.4:
    print("Underweight")
elif 18.5 <= bmi <= 24.9:
    print("Normal weight")
elif 25.0 <= bmi <= 29.9:
    print("Overweight")
else:
    print("Obese")
