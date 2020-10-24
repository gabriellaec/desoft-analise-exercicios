dependentes = int(input('Insira o número de dependentes '))
salario_bruto = int(input('Insira a salario bruto '))
if salario_bruto<=1045.00:
    contribuicaoINSS=0.075*salario_bruto
elif salario_bruto<=2089.60:
    contribuicaoINSS=0.09*salario_bruto
elif salario_bruto<=3134.40:
    contribuicaoINSS=0.12*salario_bruto
elif salario_bruto<=6101.06:
    contribuicaoINSS=0.14*salario_bruto
else:
    contribuicaoINSS=671.12
print(contribuicaoINSS)
print(salario_bruto)
base_calculo = salario_bruto - contribuicaoINSS - dependentes*189.59
print(base_calculo)
if base_calculo <= 1903.98:
    aliquota = 0
    deducao = 0
elif base_calculo<=2826.65:
    aliquota = 0.075
    deducao = 142.80
elif base_calculo <=3751.05:
    aliquota = 0.15
    deducao = 354.80
elif base_calculo<=4664.68:
    aliquota = 0.225
    deducao = 636.13
else:
    aliquota = 0.275
    deducao = 869.36
IRRF = base_calculo*aliquota-deducao
print(IRRF)