def calcula_aumento(salario):
    aumento=salario*taxa
    if salario>1250:
        taxa=1/10
        return ("aumento de ", aumento)
    else :
        taxa=15/100
        return ("aumento de  ", aumento)