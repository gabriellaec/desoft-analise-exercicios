salario = int(input('qual salário? '))
dependentes = int(input('quantos dependentes? '))

if salario <= 1045:
    inss = salario*0.075
elif salario >= 1045.01 and salario <= 2089.60:	
    inss = salario*0.09
elif salario >= 2089.61 and salario <= 3134.40:
    inss = salario*0.12
elif salario >= 3134.41 and salario <= 6101.06:
    inss = salario*0.14
elif salario > 6101.06:
    inss = 671.12
    
base = salario - inss - dependentes*189.59

if base <= 1903.98:
    aliq = 0
    dedu = 0
elif base >= 1903.99 and base <= 2826.65:
    aliq = 0.075
    dedu = 142.8
elif base >= 2826.66 and base <= 3751.05:
    aliq = 0.15
    dedu = 354.8
elif base >= 3751.06 and base <=  4664.68:
    aliq = 0,225
    dedu = 636.13
elif base > 4664.68:
    aliq = 0.275
    dedu = 869.36
    
irrf = base*aliq - dedu

print (irrf)