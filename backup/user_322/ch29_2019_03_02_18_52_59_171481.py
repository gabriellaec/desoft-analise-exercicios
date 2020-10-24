def calcula_aumento(salario):
    if salario > 1250:
        aumento = salario + (0.1 * salario)
        return aumento
    if salario <= 1250:
        aumento = salario * (1.15)
        return aumento
   