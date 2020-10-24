def calcula_aumento(salario):
    if salario > 1250:
        aumento= salario * 0.1
        return 'Houve um aumento de {0}'. format(aumento)
    else: 
        aumento= salario * 0.15
        return 'Houve um aumento de {0}'. format(aumento)