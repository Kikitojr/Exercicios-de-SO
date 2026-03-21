#Receba o número de voltas, a extensão do circuito (em metros) e o tempo de duração
#(minutos). Calcule e mostre a velocidade média em km/h.

def velocidade(tmp, dtotal):
    vel = (dtotal / (tmp / 60))
    print(vel, "Km/h")

def main():
    voltas = int(input("Digite o número de voltas:"))
    dist = int(input("Digite a distancia da pista em metros:"))
    dtotal = voltas * dist / 1000
    tmp = int(input("Digite o tempo em minutos:"))
    vel = 0

    velocidade(tmp, dtotal)

if __name__ == "__main__":
    main()