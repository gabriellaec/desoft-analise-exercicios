salario_bruto = float(input('Qual o seu salário bruto?'))
dependentes = int(input('Quantas pessoas dependem do seu salário?'))


if salario_bruto <= 1.045:
    INSS = salario_bruto * 0.075
if salario_bruto <= 2089.60:
    INSS = salario_bruto * 0.09
if salario_bruto <= 3134.40:
    INSS = salario_bruto * 0.12
if salario_bruto <= 6101.06:
    INSS = salario_bruto * 0.14
else:
    INSS = 671.12

base_do_calculo = salario_bruto - INSS - (dependentes * 189.59)
if base_do_calculo <= 1903.98:
    IRRF = (base_do_calculo * 0) - 0
if base_do_calculo <= 2826.65:
    IRRF = (base_do_calculo * 0.075) - 142.80
if base_do_calculo <= 3751.05:
    IRRF = (base_do_calculo * 0.15) - 354.80
if base_do_calculo <= 4664.68:
    IRRF = (base_do_calculo * 0.225) - 636.13
else:
    IRRF = (base_do_calculo * 0.275) - 869.36
        
print(IRRF)