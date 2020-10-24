def calcula_imposto (salario_bruto, dependentes):
# Calcula o INSS
    if salario_bruto <= 1045:
        inss = salario_bruto * 0.075
    elif salario_bruto > 1045 and salario_bruto <= 2089.6:
        inss = salario_bruto * 0.09
    elif salario_bruto > 2089.6 and salario_bruto <= 3134.4:
        inss = salario_bruto * 0.12
    elif salario_bruto > 3134.4 and salario_bruto <= 6101.06:
        inss = salario_bruto * 0.14
    else:
        inss = 671.12

# Calcula a Base de Cálculo do IRRF
    base_de_calculo = salario_bruto - inss - (dependentes * 189.59)
    
# Calcula Alíquota e Dedução
    if base_de_calculo <= 1903.98:
        aliquota = 0
        deducao = 0
    elif base_de_calculo > 1903.98 and base_de_calculo <= 2826.65:
        aliquota = base_de_calculo * 0.075
        deducao = 142.8
    elif base_de_calculo > 2826.65 and base_de_calculo <= 3751.05:
        aliquota = base_de_calculo * 0.15
        deducao = 354.8
    elif base_de_calculo > 3751.05 and base_de_calculo <= 4.664.68:
        aliquota = base_de_calculo * 0.225
        deducao = 636.13
    else:
        aliquota = base_de_calculo * 0.275
        deducao = 869.36

# Calcula IRRF
    irrf = (base_de_calculo * aliquota) - deducao

    return irrf