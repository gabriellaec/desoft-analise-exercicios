salario = float(input("Qual seu salário bruto? "))
dependentes = int(input("Quantos dependentes? "))
if salario <= 1045:
    INSS_aliquota = 0.075
    contribuicao = salario*INSS_aliquota
if salario >= 1045.01 and salario <= 2089.60:
    INSS_aliquota = 0.09
    contribuicao = salario*INSS_aliquota
if salario >= 2080.61 and salario <= 3134.40:
    INSS_aliquota = 0.12
    contribuicao = salario*0.12
if salario >= 3134.41 and salario <= 6101.06:
    INSS_aliquota = 0.14
    contribuicao = salario*INSS_aliquota
if salario > 6101.06:
    contribuicao = 671.12

    base = salario - contribuicao - dependentes*189.59


if base <= 1903.98:
    IRRF_aliquota = 0
    deducao = 0
if base >= 1903.99 and base <= 2826.65:
    IRFF_aliquota = 0.075
    deducao = 142.80
if base >= 2826.66 and base <= 3751.05:
    IRFF_aliquota = 0.15
    deducao = 354.80
if base >= 3751.06 and base <= 4664.68:
    IRFF_aliquota = 0.225
    deducao = 636.13
if base > 4664.68:
    IRFF_aliquota = 0.275
    deducao = 869.36

IRFF = base*IRFF_aliquota - deducao

print(IRFF)