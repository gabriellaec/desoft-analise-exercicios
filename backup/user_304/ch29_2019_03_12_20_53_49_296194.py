salario=int(input('qual é o seu salario? '))
def calcula_aumento (salario):
    if salario> 1250:
        a=salario*0.1
    else:
        a=salario*0.15
    return a
print('seu aumento é de {0}'.format (calcula_aumento(salario)))