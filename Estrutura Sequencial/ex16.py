#Receba a quantidade de horas trabalhadas, o valor por hora, o percentual de desconto e o número de dependentes. Calcule o salário que serão as horas trabalhadas x o valor por hora. Calcule o salário líquido (= Salário Bruto – desconto). A cada dependente será acrescido R$ 100 no Salário Líquido. Exiba o salário a receber.
#declarar
horast = int(input("Digite a quantidade de horas trabalhadas:"))
horasv = int(input("Digite valor por hora:"))
desc = int(input("Digite o percentual de desconto:"))
desc = 1 - (desc / 100)
dep = int(input("Digite o número de dependentes:"))
salariob = 0
salariol = 0
#início
salariob = horast * horasv
salariol = (salariob * desc) + 100 * dep
print("O salário a receber é:", salariol)
#fim
