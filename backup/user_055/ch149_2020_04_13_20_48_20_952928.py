salario = float(input('Qual é o seu salário bruto?: '))
dependentes = int(input('Quantos dependentes você tem?: '))
if salario <= 1045.00:
    contribuicao = (salario * 0.075)
if salario >= 1045.01 and salario <= 2089.60:
    contribuicao = (salario * 0.09)
if salario >= 2089.61 and salario <= 3134.40:
    contribuicao = (salario * 0.12)
if salario >= 3134.41 and salario <= 6101.06:
    contribuicao = (salario * 0.14)
if salario > 6101.06:
    contribuicao = 671.12
base_irrf = (salario - contribuicao - (dependentes * 189.59))
if base_irrf <= 1903.98:
    aliquota = 0
    deducao = 0
if base_irrf >= 1903.99 and base_irrf <= 2826.65:
    aliquota = 0.075
    deducao = 142.80
if base_irrf >= 2826.66 and base_irrf <= 3751.05:
    aliquota = 0.15
    deducao = 354.80
if base_irrf >= 3751.06 and base_irrf <= 4664.68:
    aliquota = 0.225
    deducao = 636.13
if base_irrf > 4664.68:
    aliquota = 0.275
    deducao = 869.36
irrf = (base_irrf * aliquota - deducao)
print(irrf)