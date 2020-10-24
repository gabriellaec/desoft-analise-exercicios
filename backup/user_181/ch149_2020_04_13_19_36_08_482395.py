salario = float(input('Qual eh seu salario bruto? '))
dependentes = int(input('Qual eh o numero de dependentes que voce possui? '))

if salario <= 1045.00:
    taxa = 0.075
    contribuicao = salario * taxa
    base = salario - contribuicao - dependentes * 189.59
    
if salario > 1045.00 and salario <= 2089.60:
    taxa = 0.09
    contribuicao = salario * taxa
    base = salario - contribuicao - dependentes * 189.59

if salario > 2089.60 and salario <= 3134.40:
    taxa = 0.12
    contribuicao = salario * taxa
    base = salario - contribuicao - dependentes * 189.59

if salario > 3134.40 and salario <= 6101.06:
    taxa = 0.12
    contribuicao = salario * taxa
    base = salario - contribuicao - dependentes * 189.59

if salario > 6101.06:
    taxa = 0.12
    base = salario - 671.12 - dependentes * 189.59


if base <= 1903.98:
    taxa = 0.00
    deducao = 0.00
    IRRF = base * taxa - deducao

if base > 1903.98 and base <= 2826.65:
    taxa = 0.075
    deducao = 142.80
    IRRF = base * taxa - deducao

if base > 2826.65 and base <= 3751.05:
    taxa = 0.15
    deducao = 354.80
    IRRF = base * taxa - deducao

if base > 3751.05 and base <= 4664.68:
    taxa = 0.225
    deducao = 636.13
    IRRF = base * taxa - deducao

if base > 4664.68:
    taxa = 0.275
    deducao = 869.36
    IRRF = base * taxa - deducao

print(IRRF)