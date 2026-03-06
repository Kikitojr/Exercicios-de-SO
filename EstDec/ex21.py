#Receba 4 notas bimestrais de um aluno. Calcule e mostre a média aritmética. Mostre a mensagem de acordo com a média:
#declarar  
nota1 = float(input("Digite a nota do primeiro aluno:")) #Nota do primeiro aluno
nota2 = float(input("Digite a a nota do segundo aluno:")) #Nota do segundo aluno
nota3 = float(input("Digite a nota do terceiro aluno:")) #Nota do terceiro aluno
nota4 = float(input("Digite a nota do quarto aluno:"))   #Nota do quarto aluno
media = 0
#início
media = ((nota1 + nota2 + nota3 + nota4) / 4)
if (media >= 6):
    print("APROVADO")
elif (media >= 3):
      print("EXAME")
else:
     print("REPROVADO")
#fim
