salario_bruto = float(input('Digite seu salário bruto: '))
dependentes = int(input('Digite a quantidade de dependentes: '))
if salario_bruto <= 1045.00:
    INSS = salario_bruto * 0.075
elif 1045.01 <= salario_bruto <= 2089.60:
    INSS = salario_bruto * 0.09
elif 2089.61 <= salario_bruto <= 3134.40:
    INSS = salario_bruto * 0.12
elif 3143.41 <= salario_bruto <= 6101.06:
    INSS = salario_bruto * 0.14
else:
    INSS = 671.12

# A base do cálculo do IRFF (objetivo) é BASE DE CALCULO = SALARIO BRUTO - INSS - Nº DE DEPENDENTES * 189.59 = 8949.70

base_de_calculo = salario_bruto - INSS - (dependentes * 189.59)

if base_de_calculo <= 1903.98:
    IRFF = base_de_calculo * 0 - 0
    print(IRFF)
elif 1903.99 <= base_de_calculo <= 2826.65:
    IRFF = base_de_calculo * 0.75 - 142.80
    print(IRFF)
elif 2826.66 <= base_de_calculo <= 3751.05:
    IRFF = base_de_calculo * 1.5 - 354.80
    print(IRFF)
elif 3751.06 <= base_de_calculo <= 4664.68:
    IRFF = base_de_calculo * 2.25 - 636.13
    print(IRFF)
else:
    IRFF = base_de_calculo * 2.75 - 869.36
    print(IRFF)