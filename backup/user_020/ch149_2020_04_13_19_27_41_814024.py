salario = float(input("Qual o seu salário? "))
dependentes = int(input("Insira o número de dependentes: "))

if salario <= 1045.00:
    inss = salario * 0.075
elif 2089.60 >= salario >= 1045.01:
    inss = salario * 0.09
elif 3134.4 >= salario >= 2089.61:
    inss = salario * 0.12
elif 6101.06 >= salario >= 3134.41:
    inss = salario * 0.14
else:
    inss = 671.12
    
base_de_calculo = salario - inss - (dependentes*189.59)

if base_de_calculo <= 1903.98:
    deducao = 0
    aliquota = 0
elif 2826.65 >= base_de_calculo >= 1903.99:
    deducao = 142.8
    aliquota = 0.075
elif 3751.05 >= base_de_calculo >= 2826.66:
    deducao = 354.8
    aliquota = 0.15
elif 4664.68 >= base_de_calculo >= 3751.06:
    deducao = 636.13
    aliquota = 0.225
else:
    deducao = 869.36
    aliquota = 0.275
    
irrf = (base_de_calculo*aliquota) - deducao

print(base_de_calculo)    
print(irrf)