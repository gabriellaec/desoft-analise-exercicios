salario_bruto = float(input('Qual o salário bruto?'))
dependentes = int(input('Qual o número que dependentes?'))
def inss(salario_bruto, dependentes):
    if salario_bruto <= 1045.00:
        INSS = salario_bruto * 0.075
        return INSS
    elif salario_bruto > 1045.00 and salario_bruto <= 2089.60:
        INSS = salario_bruto * 0.09
        return INSS
    elif salario_bruto > 2089.60 and salario_bruto <=3134.40:
        INSS = salario_bruto * 0.12
        return INSS
    elif salario_bruto > 3134.40 and salario_bruto <= 6101.06:
        INSS = salario_bruto * 0.14
        return INSS
    elif salario_bruto > 6101.06:
        INSS = 671.12
        return INSS
    
    base_de_calculo = salario_bruto - INSS - (dependentes *189.59)

    if base_de_calculo <= 1903.98:
        aliquota = 0
        deducao = 0
        return aliquota
        return deducao
    elif base_de_calculo > 1903.98 and base_de_calculo <= 2826.65:
        aliquota = 0.075
        deducao = 142.80
        return aliquota
        return deducao
    elif base_de_calculo > 2826.65 and base_de_calculo <= 3751.05:
        aliquota = 0.15
        deducao = 354.80
        return aliquota
        return deducao
    elif base_de_calculo > 3751.05 and base_de_calculo <= 4664.68:
        aliquota = 0.225
        deducao = 636.13
        return aliquota
        return deducao
    elif base_de_calculo > 4664.68:
        aliquota = 0.275
        deducao = 869.36
        return aliquota
        return deducao
    IRRF = (base_de_calculo*aliquota) - deducao
    return IRRF 
print (inss(salario_bruto, dependentes))