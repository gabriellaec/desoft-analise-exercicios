def calcula_aumento(salario):
    taxa=1/10
    aumento=salario*taxa
    if salario>1250:
        aumento=salario*taxa
        return ("aumento de ", aumento)
    else :
        aumento=salario*(taxa+5/100)
        return ("aumento de  ", aumento)