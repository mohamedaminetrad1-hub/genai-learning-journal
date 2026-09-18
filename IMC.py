#This program calculates IMC from weight and height
weight = input ('Enter you weigth in kg = ')
height = input ('Enter your height in m = ')
imc = float(weight) / (float(height) ** 2)
print("Your IMC is: " + str(imc))