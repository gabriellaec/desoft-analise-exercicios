#salario e dependentes
salario = float(input('Qual é o seu salário bruto? '))
dependentes = int(input('Qual é o número de dependentes? '))

# contribuição para o INSS
if salario <= 1045:
    aliquota = 0.075
    contribuicao = salario * aliquota 
elif salario >= 1045.01 and salario <= 2089.60:
    aliquota = 0.09
    contribuicao = salario * aliquota
elif salario >= 2089.61 and salario <= 3134.40:
    aliquota = 0.12
    contribuicao = salario * aliquota
elif salario >= 3134.41 and salario <= 6101.06:
    aliquota = 0.14
    contribuicao = salario * aliquota
else:
    contribuicao = 671.12

print(contribuicao)

#base de cálculo do IRRF simplificado
base = salario - contribuicao - dependentes * 189.59

print(base)

#IRRF simplificado
if base <= 1903.98:
    aliquota = 0
    deducao = 0
    IRRF = base*aliquota - deducao
elif base >= 1903.99 and base <= 2826.65:
    aliquota = 0.075
    deducao = 142.80
    IRRF = base*aliquota - deducao
elif base >= 2826.66 and base <= 3751.05:
    aliquota = 0.15
    deducao = 354.80
    IRRF = base*aliquota - deducao
elif base >= 3751.06 and base <= 4664.68:
    aliquota = 0.225
    deducao = 636.13
    IRRF = base*aliquota - deducao
else:
    aliquota = 0.275
    deducao = 869.36
    IRRF = base*aliquota - deducao

print(IRRF)