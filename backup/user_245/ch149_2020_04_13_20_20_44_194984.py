sal = float(input("Qual o seu salário? "))
num_dependentes = int(input("Insira o número de dependentes: "))

if sal <= 1045.00:
    INSS = sal * 0.075
elif 2089.60 >= sal >= 1045.01:
    INSS = sal * 0.09
elif 3134.4 >= sal >= 2089.61:
    INSS = sal * 0.12
elif 6101.06 >= sal >= 3134.41:
    INSS = sal * 0.14
else:
    INSS = 671.12

calculo_de_base = sal - INSS - (num_dependentes*189.59)

if calculo_de_base <= 1903.98:
    ded = 0
    aliquota_bc = 0
elif 2826.65 >= calculo_de_base >= 1903.99:
    ded = 142.8
    aliquota_bc = 0.075
elif 3751.05 >= calculo_de_base >= 2826.66:
    ded = 354.8
    aliquota_bc = 0.15
elif 4664.68 >= calculo_de_base >= 3751.06:
    ded = 636.13
    aliquota_bc = 0.225
else:
    ded = 869.36
    aliquota_bc = 0.275

IRRF = (calculo_de_base*aliquota_bc) - ded

print(IRRF)