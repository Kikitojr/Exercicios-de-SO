#Receba a temperatura em graus Celsius. Calcule e mostre a sua temperatura convertida em fahrenheit F = (9*C+160) /5.
#declarar
celcius = int(input("Digite a temperatura em graus celcius:"))
f = 0
#inicio
f = (9*celcius + 160) / 5
print("Sua temperatura em fahrenheit é:",f)