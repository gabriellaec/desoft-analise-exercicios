salario = float(input('Qual o salario bruto? '))
dependentes = int(input('Número de dependentes: '))
if salario <= 1045.00:
    INSS = salario * 0.075
elif salario >= 1045.01 and salario <= 2089.60:
    INSS = salario * 0.09
elif salario >= 2089.61 and salario <= 3134.40:
    INSS = salario * 0.12
elif salario >= 3134.41 and salario <= 6101.06:
    INSS = salario * 0.14
else:
    INSS = 671.12
BC = salario - INSS - (dependentes * 189.59)
if BC < 1903.98:
    AL = 0
    deducao = 0
elif BC >= 1903.99 and BC <= 2826.65:
    AL = 0.075
    deducao = 142.80
elif BC >= 2826.66 and BC <= 3751.05:
    AL = 0.15
    deducao = 354.80
elif BC >= 3751.06 and BC <= 4664.68:
    AL = 0.225
    deducao = 636.13
else:
    AL = 0.275
    deducao = 869.36
IRRF = (BC * AL) - deducao
print('Seu IRRF simplificado é {0}'.format(IRRF))