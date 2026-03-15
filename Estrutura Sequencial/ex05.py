#Receba os coeficientes A, B e C de uma equação do 2º grau (AX²+BX+C=0). Calcule e mostre as raízes reais (considerar que a equação possue2 raízes).
import math
print("Essa é a estrutura de um equação do 2º grau (AX²+BX+C=0)")
#declarar       
a = float(input("Digite o coeficiente A:"))
b = float(input("Digite o coeficiente B:"))
c = float(input("Digite o coeficiente C:"))
result = 0
delta = 0
#início
delta = pow(b, 2) - 4*a*c
if delta < 0:
    print("Não existem raizes reais")
else:
    raiz = math.sqrt(delta)
    print("Raiz de delta é:",raiz)
    x1 = (-b + raiz) / (2*a)
    x2 = (-b - raiz) / (2*a)
    
    print("Suas raizes são:", x1, x2)
#fim
