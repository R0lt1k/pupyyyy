def bmi_calculator(weight, height):
    return weight / (height /100)**2

weight = float(input("ENt ur weigt in kg: "))
height = float(input("ENt ur height in cm: "))

bmi = bmi_calculator(weight, height)

if bmi < 18.5:
    print(f'у вас недовес,  ваш показатель bmi = {bmi}')
elif bmi > 18.5 and bmi < 24.9:
    print(f'Все отлично,  ваш показатель bmi = {bmi}')
else:
    print(f'у вас перевес,  ваш показатель bmi = {bmi}')