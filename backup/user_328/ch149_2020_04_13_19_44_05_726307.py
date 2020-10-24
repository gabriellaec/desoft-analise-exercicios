sal= float(input('Qual seu salário bruto? '))
dep= int(input('Quantas pessoas dependem do seu salário? '))
if sal <= 1045.00:
    inss= sal*0.075
elif sal <= 2089.60:
    inss= sal*0.09
elif sal <= 3134.40:
    inss= sal*0.12
elif sal <= 6101.06:
    inss= sal*0.14
else:
    inss= 671.12
base_de_calculo= sal - inss - (dep*189.59)
if base_de_calculo <= 1903.98:
    y=0
    x=0
elif base_de_calculo <= 2826.65:
    y=0.075
    x=142.80
elif base_de_calculo <= 3751.05:
    y= 0.15
    x= 354.80
elif base_de_calculo <= 4664.68:
    y= 0.225
    x= 636.13
else:
    y= 0.275
    x= 869.36
Irrf= (base_de_calculo*y)-x
print(Irrf)