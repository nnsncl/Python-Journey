height = 1.88
weigth = 88.4
bmi = weigth / height ** 2


if bmi <= 25:
    print(f'Your BMI is {bmi}: Average')
elif bmi >25 and bmi <= 35:
   print(f'Your BMI is {bmi}: Overweight')
elif bmi > 35:
    print(f'Your BMI is {bmi}: Obesity')
else:
    print(f'Your BMI is {bmi}')