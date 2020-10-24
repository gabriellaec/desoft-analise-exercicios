salario=float(input("Qual o salario bruto?"))
numero=int(input('Qual o número de dependentes do usuário?'))
imposto=0
base_de_calculo=0
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

    
base_de_calculo = salario - imposto - numero * 189,59
IRFF=base_de_calculo*aliquota-deducao