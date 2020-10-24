salario = float(input('Qual o seu salario: '))
dependentes = int(input('Numero de dependentes: '))

#Aliquota
if salario <= 1045:
    Aliquota = 0.075
    #contribuição
    contribui = salario*Aliquota
    
elif salario > 1045 and salario <= 2089.60:
    Aliquota = 0.09
    #contribuição
    contribui = salario*Aliquota
    
elif salario > 2089.61 and salario <= 3134.40:
    Aliquota = 0.12
    #contribuição
    contribui = salario*Aliquota
    
elif salario > 3134.41 and salario <= 6101.06:
    Aliquota = 0.14
    #contribuição
    contribui = salario*Aliquota
    
elif salario > 6101.06:
    contribui = 671.12



#Base
base = salario - contribui - (dependentes*189.59)


#dedução
if salario <= 1903.98:
    Aliquota2 = 0
    #contribuição
    deducao = 0
    
elif salario > 1903.88 and salario <= 2826.65:
    Aliquota2 = 0.075
    #contribuição
    deducao = 142.80
    
elif salario > 2826.66 and salario <= 3751.05:
    Aliquota2 = 0.15
    #contribuição
    deducao = 354.80
    
elif salario > 3751.06 and salario <= 4664.68:
    Aliquota2 = 0.225
    #contribuição
    deducao = 636.13
    
elif salario > 4664.68:
    Aliquota2 = 0.275
    deducao = 869.36

#IRRF
IR = (base * Aliquota2) - deducao

print(IR)