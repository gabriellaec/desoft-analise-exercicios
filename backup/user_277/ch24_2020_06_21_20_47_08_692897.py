def calcula_aumento(salario):
    if salario>1250:
        k = 0.1 * salario
    else:
        k = 0.15 * salario
    return k