salario=float(input("Qual o salario bruto?"))
numero=int(input('Qual o número de dependentes do usuário?'))

#INSS
if salario<=1045:
    imposto=0.075*salario
elif salario>1045.01 and salario<=2089.6:
    imposto=0.09*salario
elif salario>2089.61 and salario<=3134.4:
    imposto=0.12*salario
elif salario>3134.41 and salario<=6101.06:
    imposto=0.14*salario
else:
    imposto=671.12
    
    
base_de_calculo = salario - imposto - numero * 189.59

if base_de_calculo<1903.98:
    ded=0.0
elif 1903.99<=base_de_calculo<=2826.65:
    ded=142.8
elif 2826.66<=base_de_calculo<=3751.05:
    ded=354.8
elif 3751.66<=base_de_calculo<=4664.68:
    ded=636.13
else:
    ded=869.36

if base_de_calculo<1903.98:
    ali=0.0
elif 1903.99<=base_de_calculo<=2826.65:
    ali=0.075
elif 2826.66<=base_de_calculo<=3751.05:
    ali=0.15
elif 3751.66<=base_de_calculo<=4664.68:
    ali=0.225
else:
    ali=0.275
    

IRFF=base_de_calculo*ali-ded
print(IRFF)