def calcula_aumento(salario):
    valor = 0
    if (salario > 1250):
        valor = salario * 1.1
        return valor
    else:
        valor = salario*1.15
        return valor
