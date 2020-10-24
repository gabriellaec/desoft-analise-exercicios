Salario = float(input('Qual é o seu salário bruto: '))
dependentes = float(input('Qual é o seu número de dependentes: '))
if Salario >= 2089.61 and Salario <= 3134.40:
    Inss = Salario*0.12
elif Salario >= 3134.42 and Salario <= 6106.06:
    Inss = Salario*0.14
elif Salario <= 1045:
    Inss = Salario*0.075
elif Salario >= 1045.01 and Salario <= 2089.6:
    Inss = Salario*0.09
else:
    Inss = 671.12    
Base_de_Calculo = Inss - Salario - (dependentes*189.59)
if Base_de_Calculo >= 2826.66 and Base_de_Calculo <= 3751.05:
    Irrf = (Base_de_Calculo*0.15) - 354.8
elif Base_de_Calculo >= 1903.99 and Base_de_Calculo <= 2826.65:
    Irrf = (Base_de_Calculo*0.075) - 142.8
elif Base_de_Calculo <= 1903.98:
    Irrf = (Base_de_Calculo*0) 
elif Base_de_Calculo >= 3751.06 and Base_de_Calculo <= 4664.68:
    Irrf = (Base_de_Calculo*0.225) - 636.13
else:
    Irrf = (Base_de_Calculo*0.275) - 869.36
print (Irrf)