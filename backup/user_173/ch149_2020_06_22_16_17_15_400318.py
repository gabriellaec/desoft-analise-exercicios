salario = float(input('Escreva seu salário bruto: '))
dependentes = int(input('Escreva o seu número de dependentes: '))
if salario <= 1045:
    inss = salario*0.075
elif salario >= 1045.01 and salario <= 2089.6:
    inss = salario*0.09
elif salario >= 2089.61 and salario <= 3134.40:
    inss = salario*0.12
elif salario >= 3134.42 and salario <= 6106.06:
    inss = salario*0.14
else:
    inss = 671.12    
base_de_calculo = salario - inss - (dependentes*189.59)

if base_de_calculo <= 1903.98:
    irrf = (base_de_calculo*0)+0
elif base_de_calculo >= 1903.99 and base_de_calculo <= 2826.65:
    irrf = (base_de_calculo*0.075)-142.8
elif base_de_calculo >= 2826.66 and base_de_calculo <= 3751.05:
    irrf = (base_de_calculo*0.15)-354.8
elif base_de_calculo >= 3751.06 and base_de_calculo <= 4664.68:
    irrf = (base_de_calculo*0.225)-636.13
else:
    irrf = (base_de_calculo*0.275)-869.36

print (irrf)