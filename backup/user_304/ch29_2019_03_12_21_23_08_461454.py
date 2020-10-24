salario=float(input('qual é o seu salario? '))
def calcula_aumento(salario):
    if salario> 1250:
        a=salario*0.1
    else:
        a=salario*0.15
    return a
x=calcula_aumento(salario)
print('seu aumento é de {0}'.format(x))