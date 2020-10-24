salario=float(input("Qual o salario bruto?"))
numero=float(input('Qual o número de dependentes do usuário?'))
imposto=0
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
             