valor_salario = float(input("Qual o valor de seu salário bruto?"))
numero_dependentes = float(input("Quantos dependentes você possui?"))


def contribuicao_inss(salariobruto):
    if salariobruto <= 1045.00:
        return salariobruto*0.075
    elif salariobruto >= 1045.01 and salariobruto <= 2089.60:
        return salariobruto*0.09
    elif salariobruto >= 2089.61 and salariobruto <= 3134.40:
        return salariobruto*0.12
    elif salariobruto >= 3134.41 and salariobruto <= 6101.06:
        return salariobruto*0.14
    else:
        return 671.12


def base_calculo(salariobruto, contribuicao, dependentes):
    return salariobruto-contribuicao-dependentes*189.59


def aliquota_deducao(base_calculo):
    if base_calculo <= 1903.98:
        return 0, 0
    elif base_calculo >= 1903.99 and base_calculo <= 2826.65:
        return 0.075, 142.80
    elif base_calculo >= 2826.66 and base_calculo <= 3751.05:
        return 0.15, 354.80
    elif base_calculo >= 3751.06 and base_calculo <= 4664.68:
        return 0.225, 636.13
    else:
        return 0.275, 869.36


base_calculo_valor = base_calculo(
    valor_salario, contribuicao_inss(valor_salario), numero_dependentes)
aliquota_deducao_valor = aliquota_deducao(base_calculo_valor)

irrf = base_calculo_valor*aliquota_deducao_valor[0] - aliquota_deducao_valor[1]
print(irrf)
