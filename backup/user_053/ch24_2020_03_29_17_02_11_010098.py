salario_recebido = float(input('Valor do Salário: R$ '))

def calcula_aumento(salario):
    if salario > 1250:
        aumento = 0.1*salario
    else:
        aumento = 0.15*salario

    return aumento


a=calcula_aumento(salario_recebido)
print(a)