salariobruto = float(input("Qual é o salário bruto?"))
numerodedependentes = int(input("Quantos são seus dependentes?"))


if salariobruto < 1045:
    contirbuicao = salariobruto*(0.075)
if 1045.01 < salariobruto < 2089.6:
    contirbuicao = salariobruto*(0.09)
else:
    if 2089.61 < salariobruto < 3134.4:
        contirbuicao = salariobruto*(0.12)
    elif 3134.41 < salariobruto < 6101.06:
        contribuicao = salariobruto*(0.14)
    else:
        contribuicao = 671.12

basedecalculo = salariobruto - contribuicao - (numerodedependentes * 189.59)

if basedecalculo < 1903.98:
    aliquota = 0
    deducao = 0
if 1903.99 < basedecalculo < 2826.65:
    aliquota = 0.075
    deducao = 142.8
else:
    if 2826.66 < basedecalculo < 3751.05:
        aliquota = 0.15
        deducao = 354.80
    elif 3751.06 < basedecalculo < 4664.68:
        aliquota = 0.225
        deducao = 636.13
    else:
        aliquota = 0.275
        deducao = 869.36
irrf = (basedecalculo*aliquota)-deducao
print(irrf)