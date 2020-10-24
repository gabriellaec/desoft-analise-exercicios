salario = int(input('Qual o seu salário? ')
dependentes = int(input('Quantos dependentes você tem? ')

if salario <= 1045:
    contribuicao = salario*0.075
if salario >= 1045.01 and salario <= 2089.60:
    contribuicao = salario*0.09
if salario >= 2089.01 and salario <= 3134.40:
    contribuicao = salario*0.12
if salario >= 3134.41 and salario <= 6101.06:
    contribuicao = salario*0.14
if salario > 6101.06:
    contribuicao = 671.12

base = salario - contribuicao - dependentes*189.59

if base <= 1903.98:
    IRRF = base*0.0 - 0
if base >= 1903.99 and base <= 2826.65:
    IRRF = base*0.075 - 142.80
if base >= 2826.66 and base <= 3751.05:
    IRRF = base*0.15  - 354.80
if base >= 3751.06 and base <= 4664.68:
    IRRF = base*0.225 - 636.13
if base > 4664.68:
    IRRF = base*0.275 - 869.36
                   
print(IRRF)

                  