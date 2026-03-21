#Receba o tipo de investimento (1 = poupança e 2 = renda fixa) e o valor do investimento.
#Calcule e mostre o valor corrigido em 30 dias sabendo que a poupança = 3% e a renda fixa = 5%.
#Demais tipos não serão considerados.#Receba o tipo de investimento (1 = poupança e 2 = renda fixa) e o valor do investimento.
#Calcule e mostre o valor corrigido em 30 dias sabendo que a poupança = 3% e a renda fixa = 5%.
#Demais tipos não serão considerados.

def investimento(valor, invest):
    if invest == 1:
        res = valor * 1.03
        print(res)
    elif invest == 2:
        res = valor * 1.05
        print(res)
    else:
        print("Digite 1 ou 2") 

def main():
    invest = int(input("Digite 1 para poupança e 2 para enda fixa:"))
    valor = float(input("Valor do investimento:"))

    investimento(valor, invest)

if __name__ == "__main__":
    main()
