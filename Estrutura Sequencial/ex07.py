#Receba os valores do comprimento, largura e altura de um paralelepípedo. Calcule e mostre seu volume.
#declarar
larg = int(input("Digite a largura do paralelepipedo em litros:"))
alt = int(input("Digite a altura do paralelepipedo em litros:"))
comp = int(input("Digite o comprimento do paralelepipedo em litros:"))
#início
vol = alt * larg * comp
print("O volume do paralelepipedo é:", vol,"m3")
#fim