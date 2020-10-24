#Cálculo IRRF 
salario_bruto = float(input('Digite o Salário Bruto: '))
dependentes = int(input('Digite a quantidade de dependentes: '))
#Cálculo da contribuição
contribuicao = 0
if salario_bruto <= 1045:
    contribuicao = salario_bruto*0.075 
elif salario_bruto > 1045.00 and salario_bruto <= 2089.60:
    contribuicao = salario_bruto*0.09
elif salario_bruto >= 2089.61 and salario_bruto <= 3134.40:
    contribuicao = salario_bruto*0.12
elif salario_bruto >= 3134.41 and salario_bruto <= 6101.06:
    contribuicao = salario_bruto*0.14
elif salario_bruto > 6101.06:
    contribuicao = 671.12
print('A contribuição é de R${0:.2f}'.format(contribuicao)) 
#Cálculo da Base de Cálculo
base_de_calculo = salario_bruto - contribuicao - (dependentes*189.59)
print('A base de cálculo é igual a R${0:.2f}'.format(base_de_calculo))
#Cálculo do IRRF
if base_de_calculo <= 1903.98:
    irrf = (base_de_calculo * 0) - 0
elif base_de_calculo >= 1903.99 and base_de_calculo <= 2826.65:
    irrf = (base_de_calculo * 0.075) - 142.80
elif base_de_calculo >= 2826.66 and base_de_calculo <= 3751.05:
    irrf = (base_de_calculo * 0.15) - 354.80
elif base_de_calculo >= 3751.06 and base_de_calculo <= 4664.68:
    irrf = (base_de_calculo * 0.225) - 636.13
elif base_de_calculo > 4664.68:
    irrf = (base_de_calculo * 0.275) - 869.36

print('O IRRF é de R${0:.2f}'.format(irrf))