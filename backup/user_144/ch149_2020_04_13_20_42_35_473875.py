salario_bruto = float(input(("Salario: "))
numero = int(input("Dependentes: "))

contri_INSS = 0
if salario_bruto <= 1045:
    contri_INSS = salario_bruto * 0.075
    
elif salario_bruto >= 1045.01 and salario_bruto <=2089.60:
    contri_INSS = salario_bruto * 0.09
    
elif salario_bruto >= 2089.01 and salario_bruto <= 3134.40:
    contri_INSS = salario_bruto * 0.12

elif salario_bruto >= 3134.41 and salario_bruto <=6101.06:
    contri_INSS = salario_bruto * 0.14
    
else:
    contri_INSS = 671.12
    
base = salario_bruto - contri_INSS - (numero* 189.59)
aliquota = 0
deducao = 0

if base <= 1903.98:
    aliquota = 0
    deducao = 0
    
elif base >= 1903.99 and base <= 2826.65:
    aliquota = 0.75
    deducao = 142.80

elif base >= 2826.66 and base <= 3751.05:
    aliquota = 0.15
    deducao = 354.80
    
elif base >= 3751.06 and base <= 4664.68:
    aliquota = 0.225
    deducao = 636.13
    
else:
    aliquota = 0.275
    deducao = 869.36
    
IRRF = base * aliquota - deducao

print(IRRF)