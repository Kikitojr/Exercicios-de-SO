#Receba 2 ângulos de um triângulo. Calcule e mostre o valor do 3º ângulo.
#declarar
ang1 = int(input("Digite o primeiro ângulo do triângulo:"))
ang2 = int(input("Digite o segundo ângulo do triângulo:"))
ang3 = 0
#início 
ang3 = 180 - ang1 - ang2
print("O valor do 3º ângulo é:", ang3)