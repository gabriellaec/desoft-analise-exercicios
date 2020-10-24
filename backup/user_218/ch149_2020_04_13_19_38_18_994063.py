salario_bruto = float(input('Qual o seu salário bruto?'))
dependentes = int(input('Quantas pessoas dependem do seu salário?'))

def INSS(salario_bruto):
    if salario_bruto <= 1.045.00:
        INSS = salario_bruto * 0.075
    if salario_bruto <= 2.089,60:
        INSS = salario_bruto * 0.09
    if salario_bruto <= 3.134.40:
        INSS = salario_bruto * 0.12
    if salario_bruto <= 6.101.06:
        INSS = salario_bruto * 0.14
    else:
        INSS = salario_bruto + 671,12

def base_do_calculo(salario_bruto, INSS, dependentes):
    x = salario_bruto - INSS - (dependentes * 189,59)
    return x

def IRRF(base_do_calculo):
    if base_do_calculo <= 1.903.98:
        IRRF = base_do_calculo * 0 - 0
    if base_do_calculo <= 2.826.65:
        IRRF = base_do_calculo * 0.075 - 142,80
    if base_do_calculo <= 3.751.05:
        IRRF = base_do_calculo * 0.15 - 354,80
    if base_do_calculo <= 4.664.68:
        IRRF = base_do_calculo * 0.225 - 636,13
    else:
        IRRF = base_do_calculo * 0.275 - 869,36
        
print(IRRF)