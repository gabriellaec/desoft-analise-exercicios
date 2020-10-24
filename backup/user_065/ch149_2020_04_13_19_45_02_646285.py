salario = 0
salario = float(input("Qual o seu salario bruto?"))
dependentes = 0
dependentes = float(input("Quantos denpendentes?"))


if salario <= 1045.00:
    aliquota = 0.075
if 1045.00 < salario <= 2089.60:
    aliquota = 0.09
if 2089.60 < salario <= 3134.40:
    aliquota = 0.12
if 3134.40 < salario <= 6101.06:
    aliquota = 0.14
elif salario > 6101.06:
    aliquota = 671.12


if aliquota < 1:
    contribuiucao = salario * aliquota
    base = salario - contribuiucao - (dependentes * 189.59)
if aliquota > 1:
    contribuiucao = aliquota
    base = salario - contribuiucao - (dependentes * 189.59)


if base <= 1903.98:
    deducao = 0.0
    aliquota = 0.0
if 1903.98 < base <= 2826.65:
    deducao = 142.80
    aliquota = 0.075
if 2826.65 < base <= 3751.05:
    deducao = 354.80
    aliquota = 0.15
if 3751.05 < base <= 4664.68:
    deducao = 636.13
    aliquota = 0.225
elif base > 466.68:
    deducao = 869.36
    aliquota = 0.275

IRRF = (base * aliquota) - deducao
if IRRF < 0:
    IRRF = IRRF * -1
if IRRF == -0.0
    IRRF = 0.0
print(IRRF)