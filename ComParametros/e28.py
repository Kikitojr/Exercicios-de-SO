#Receba o preço atual e a média mensal de um produto. Calcule e mostre o novo preço
def newprice(vendaMes, preço1):
    if (vendaMes < 500) and (preço1 < 30):
        preço2 = preço1 * 1.10
        print("O novo preço será:", preço2)
    elif (vendaMes >= 500) and (vendaMes < 1000) and (preço1 >= 30) and (preço1 < 80):
        preço2 = preço1 * 1.15
        print("O novo preço será:", preço2)
    elif (vendaMes >= 1000) and (preço1 >= 80):
        preço2 = preço1 * 0.95
        print("O novo preço será:", preço2)

def main():
    preço1 = int(input("Digite o preço inicial do produto:"))
    vendaMes = int(input("Digite a venda mensal do produto:"))

    newprice(vendaMes, preço1)

if __name__ == "__main__":
    main()