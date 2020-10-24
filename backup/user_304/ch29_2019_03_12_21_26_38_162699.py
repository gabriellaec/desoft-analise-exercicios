salario=float(input('qual é o seu salario? '))
if salario> 1250:
    a=salario*0.1
else:
    a=salario*0.15
x=calcula_aumento(salario)
print('seu aumento é de {0}'.format(x))
