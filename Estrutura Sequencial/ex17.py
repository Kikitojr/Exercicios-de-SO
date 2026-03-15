#Calcule a quantidade de litros gastos em uma viagem, sabendo que o automóvel faz 12 km/l. Receber o tempo de percurso e a velocidade média.
#declarar
tempo = int(input("Digite o tempo de percurso:"))
vm = int(input("Digite a velocidade média:"))
dist = 0
litros = 0
#início
dist = tempo * vm
litros = dist / 12
print("A quantidade de litros gastos na viagem foi de:", litros)
