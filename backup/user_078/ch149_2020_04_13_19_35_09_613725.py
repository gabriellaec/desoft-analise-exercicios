}salario_bruto = float(input('Digite seu salário: '))
numero_dependentes = int(input('Digite o número de dependentes: '))
contribuicaoINSS = 0
aliquota = 0
deducao = 0

while True
    if salario_bruto <= 1.045.00:
        contribuicaoINSS = salario_bruto*0.075

    elif salario_bruto > 1.045.01 and salario_bruto < 2.089.60:
        contribuicaoINSS = salario_bruto*0.09

    elif salario_bruto > 2.089.60 and salario_bruto < 3.134.40:
        contribuicaoINSS = salario_bruto*0.12

    elif salario_bruto > 3.134.41 and salario_bruto < 6.101.06:
        contribuicaoINSS = salario_bruto*0.14

    else: #Acima de R$ 6.101,06	R$ 671,12 (valor fixo)
        contribuicaoINSS = 671.12
    break
#A base de cálculo do IRRF simplificado é dada por:
base_calculo = salario_bruto - contribuicaoINSS - numero_dependentes * 189.59

while True
    if base_calculo <= 1.903.98:
        aliquota = 0.0 and deducao = 0.00

    elif base_calculo > 1.903.99 and base_calculo < 2.826.65:
        aliquota = 0.075 and deducao = 142.80

    elif base_calculo > 2.826.66 and base_calculo < 3.751.05:
        aliquota = 0.15 and deducao = 354.80

    elif base_calculo > 3.751.06 and base_calculo < 4.664.68:
        aliquota = 0.225 and deducao = 636.13

    else:
        #Acima de R$ 4.664,68	27,5%	R$ 869,36
        aliquota = 0.275 and deducao = 869.36
    break

#Finalmente, o IRRF simplificado é dado por:
IRRF = base_calculo * aliquota - deducao

print (IRRF)