def calcula_aumento (salario):
    taxa=1/10
    aumento=salario*taxa
    if salario>1250 :
        return ("Aumento de ", aumento)
    else :
        taxa=15/10
        return ("Aumento de ", aumento)
    