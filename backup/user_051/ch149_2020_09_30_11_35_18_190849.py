salario=float(input('Qual salario bruto?'))
nd=float(input('Qual seu nemero de dependentes?'))
if salario <= 1045:
    contribuicao_INSS=salario*0.075
if 1045.01 <= salario <= 2089.60:
    contribuicao_INSS=salario*0.09
if 2089.61 <= salario <= 3134.40:
    contribuicao_INSS=salario*0.12
if 3134.41 <= salario <= 6101.06:
    contribuicao_INSS=salario*0.14
if salario > 6101.06:
    contribuicao_INSS=671.12
bc=salario-contribuicao_INSS-nd*189.59
if bc <= 1903.98:
    al=0
    deducao=0
if 1903.99 <= bc <= 2826.65:
    al=0.075
    deducao=142.80
if 2826.66 <= bc <= 3751.05:
    al=0.15
    deducao=354.80
if 3751.06 <= bc <= 4664.68:
    al=0.225
    deducao=636.13
if bc > 4664.68:
    al=0.275
    deducao=869.36
IRRF=bc*al-deducao
print(IRRF)