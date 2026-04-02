import os

valor : int = 0
dir : str = ''
arq : str = ''
caminho : str = ''

def mult(vlr, tab):
    res = vlr * tab
    return res

def grava(c, rslt):
    print(valor, "x", c, "=", rslt) 

def cria_arq(dir01, arq01, c, rslt):
    tipo: str = ''
    enc: str = ''
    caminho = dir01 + arq01

    os.makedirs(dir01, exist_ok=True)

    if (os.path.exists(dir01) and os.path.isdir(dir01)):
        tipo = 'w'
        enc = 'utf-8'
        if (os.path.exists(caminho)):
            tipo = 'a'
        with open (caminho, tipo, encoding=enc) as file:
            file.write(f"{valor} x {c} = {rslt}\n")
            os.chmod(caminho, 0o744)
    else:
        print('Diretório invalido')

def main():
    global valor, dir, arq, caminho
    contador = 1
    result = 0

    dir = '/tmp/exercicios/'
    arq = 'ex34.txt'

    valor = int(input("Digite um valor entre 1 e 10: "))

    while contador <= 10:
        result = mult(valor, contador)
        cria_arq(dir, arq, contador, result)
        #grava(contador, result)
        contador += 1


if __name__ == '__main__':
    main()