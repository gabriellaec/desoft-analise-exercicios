def calcula_aumento(salario):
    aumento=salario*taxa
    taxa=1/10
    if salario>1250:
        aumento=salario*taxa
        return ("aumento de ", aumento)
    else :
        aumento=salario*(taxa+5/100)
        return ("aumento de  ", aumento)