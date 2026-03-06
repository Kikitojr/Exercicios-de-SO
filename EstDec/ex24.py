#Receba um valor inteiro. Verifique e mostre se é divisível por 2 e 3.
#declarar
num = int(input("Digite  um numero:"))
#início
if (num % 2 == 0) and (num % 3 == 0):
    print("O numero é divisivel por 2 e 3")
elif (num % 2 == 0):
    print("O numero é divisivel por 2")
elif (num % 3 == 0):
    print("O numero é divisivel por 3")
else:
    print("Não é divisivel nem por 2 ou 3")
#fim