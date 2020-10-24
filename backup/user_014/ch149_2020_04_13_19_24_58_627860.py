salario_bruto = float(input('Qual é o salário? '))
dependentes = int(input('Qual o número de dependentes? '))
                  
#Contribuição INSS
if salario_bruto <= 1405.00:
    salario = salario_bruto - salario_bruto * 0.075
elif 1405.01 <= salario_bruto <= 2089.60:
    salario = salario_bruto - salario_bruto * 0.09
elif 2089.61 <= salario_bruto <= 3134.40:
    salario = salario_bruto - salario_bruto * 0.12
elif 3134.41 <= salario_bruto <= 6101.06:
    salario = salario_bruto - salario_bruto * 0.14
else:
    salario = salario_bruto - 671.12
                  
base_de_calculo = salario - dependentes * 189.59

#Dedução
if base_de_calculo <= 1903.98:
    dedução = 0.0
elif 1903.99 <= base_de_calculo <= 2826.65:
    dedução = 142.80
elif 2826.66 <= base_de_calculo <= 3751.05:
    dedução = 354.80
elif 3751.06 <= base_de_calculo <= 4664.68:
    dedução = 636.13
else:
    dedução = 869.36
    
#Alíquota
if base_de_calculo <= 1903.98:
    aliquota = 0.0
elif 1903.99 <= base_de_calculo <= 2826.65:
    aliquota = 0.075
elif 2826.66 <= base_de_calculo <= 3751.05:
    aliquota = 0.15
elif 3751.06 <= base_de_calculo <= 4664.68:
    aliquota = 0.225
else:
    aliquota = 0.275
    
IRRF = base_de_calculo * aliquota - dedução              