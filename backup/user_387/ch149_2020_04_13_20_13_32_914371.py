def contrib_inss(salario_bruto):
    if salario_bruto <= 1045:
        return 0.075 * salario_bruto
    elif salario_bruto > 1045 and salario_bruto <= 2089.60:
        return 0.09 * salario_bruto
    elif salario_bruto > 2089.60 and salario_bruto <= 3134.40:
        return 0.12 * salario_bruto
    elif salario_bruto > 3134.40 and salario_bruto <= 6101.06:
        return 0.14 * salario_bruto
    elif salario_bruto > 6101.06:
        return 671.12

def irrf(base_de_calculo):
    if base_de_calculo <= 1903.98:
        return 0
    elif base_de_calculo > 1903.98 and base_de_calculo <= 2826.65:
        return base_de_calculo * 0.075 - 142.80
    elif base_de_calculo > 2826.65 and base_de_calculo <= 3751.05:
        return base_de_calculo * 0.15 - 354.80
    elif base_de_calculo > 3751.05 and base_de_calculo <= 4664.68:
        return base_de_calculo * 0.225 - 636.13
    elif base_de_calculo > 4664.68:
        return base_de_calculo * 0.275 - 869.36


salario_bruto = float(input('salário bruto :'))
dependentes = int(input('dependentes :'))
base_de_calculo = 0

base_de_calculo = salario_bruto - contrib_inss(salario_bruto) - (dependentes * 189.59)
print(irrf(base_de_calculo))