def calcula_aumento(salario):
    valor = 0
    if (salario > 1250):
        valor = salario * 0.1
        return valor
    else:
        valor = salario*0.15
        return valor
