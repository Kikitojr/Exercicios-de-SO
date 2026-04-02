import os

nome: str = ''
nota1 = nota2 = nota3 = nota4 = valor_media = 0.0
dir: str = ''
arq: str = ''

def escreve_arq(dir01 , arq01, line):
    tipo: str = ''
    enc: str = ''

    caminho = dir01 + arq01
    os.makedirs(dir01, exist_ok=True)

    if (os.path.exists(dir01) and os.path.isdir(dir01)):
        tipo = 'w'
        enc = 'utf-8'
        with open (caminho, tipo, encoding=enc) as file:
            file.write(line)



def cadastro(nm, nt1, nt2, nt3, nt4, vlr_med):
    linha: str = ''
    global dir, arq

    dir = '/tmp/exercicios/'
    arq = 'ex21.txt'
    
    linha = f"{nm};\n Nota 1: {nt1};\n Nota 2: {nt2};\n Nota 3: {nt3};\n Nota 4: {nt4};\n Média: {vlr_med};\n"

    escreve_arq(dir, arq, linha)



def med(n1, n2, n3, n4, vlr_media):
    media = (n1 + n2 + n3 + n4) / 4
    print(media)
    return media

def entrada():
    global nome, nota1, nota2, nota3, nota4, valor_media
    nome = input('Digite seu nome: ')
    nota1 = float(input('Digite sua primeira nota: '))
    nota2 = float(input('Digite sua segunda nota: '))
    nota3 = float(input('Digite sua terceira nota: '))
    nota4 = float(input('Digite sua quarta nota: '))

def main():
    entrada()
    media = med(nota1, nota2, nota3, nota4, valor_media)
    cadastro(nome, nota1, nota2, nota3, nota4, media)



if __name__ == '__main__':
    main()