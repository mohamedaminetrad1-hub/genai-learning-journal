#This program calculates IMC from weight and height
weight = input ('Enter you weigth in kg = ')
height = input ('Enter your height in m = ')
if float(height) <= 0:
    print("Height must be greater than zero.")
elif float(weight) <= 0:
    print("Weight must be greater than zero.")
else:
    imc = float(weight) / (float(height) ** 2)
    print("Your IMC is: " + str(imc))