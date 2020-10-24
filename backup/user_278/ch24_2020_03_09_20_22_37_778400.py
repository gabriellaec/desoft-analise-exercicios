def calcula_aumento(salario):
    if salario>1250:
        return "{0:.2f}".format(salario*0.1)
    else:
        return "{0:.2f}".format(salario*0.15)