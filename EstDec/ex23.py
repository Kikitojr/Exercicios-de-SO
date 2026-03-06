#Receba 3 valores obrigatoriamente em ordem crescente e um 4º valor não necessariamente em ordem. Mostre os 4 números em ordem crescente.
#declarar
num1 = int(input("Digite o primeiro numero:"))
num2 = int(input("Digite o segundo numero:"))
num3 = 0
num4 = 0
#inicio
if (num2 > num1):
    num3 = int(input("Digite um terceiro numero:"))
if(num3 > num2):
    num4 = int(input("Digite o quarto numero:"))
    if (num4 < num1):
        print(num4, num1, num2, num3)
        
    elif (num4 > num1) and (num4 < num2):
        print(num1, num4, num2, num3)

    elif(num4 > num2) and (num4 < num3):
        print(num1, num2, num4, num3)   

    else:
        (num4 > num3)
        print(num1, num2, num3, num4)
#fim    