salario_bruto = int(input("Digite seu salário: "))
numero_de_dependentes = int(input("Digite o número de dependentes: "))
if salario_bruto <= 1045:
    al1 = 0.075
    INSS = salario_bruto * al1
elif 1045.01 <= salario_bruto <= 2089.60:
    al1 = 0.09
    INSS = salario_bruto * al1
elif 2089.61 <= salario_bruto <= 3134.40:
    al1 = 0.12
    INSS = salario_bruto * al1
elif 3134.41 <= salario_bruto <= 6101.06:
    al1 = 0.14
    INSS = salario_bruto * al1
else:
    INSS = 671.12

base_de_calculo = salario_bruto - INSS - numero_de_dependentes*189.59

if base_de_calculo <= 1903.98:
    al2 = 0
    dd = 0
if 1903.99 <= base_de_calculo <= 2826.65:
    al2 = 0.075
    dd = 142.80
if 2826.66 <= base_de_calculo <= 3751.05:
    al2 = 0.15
    dd = 354.80
if 3751.06 <= base_de_calculo <= 4664.68:
    al2 = 0.225
    dd = 636.13
else:
    al2 = 0.275
    dd = 869.36

IRRF = base_de_calculo * al2 - dd

print ("O valor do IRRF é R${0}".format(IRRF))