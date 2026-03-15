#Receba a quantidade de alimento em quilos. Calcule e mostre quantos dias durará esse alimento sabendo que a pessoa consome 50g ao dia.
#declarar
quilos = int(input("Digite a quantidade de alimento em Kg: "))
dias = 0
gramas = quilos * 1000
#início
dias = gramas / 50
print("Sabendo que vc consomme 50g por dia, essa quantidade de alimento durará", dias, "dias")
