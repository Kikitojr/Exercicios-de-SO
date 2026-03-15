#Receba os valores de 2 catetos de um triângulo retângulo. Calcule e mostre a hipotenusa.
#declarar´
import math
cat1 = int(input("Digite o valor do primeiro cateto:"))
cat2 = int(input("Digite o valor do segundo cateto:"))
hip = 0
#início
hip = pow(cat1, 2) + pow(cat2, 2)
hip = hip / math.sqrt(hip)
print("A hipotenusa do triângulo é:", hip)
