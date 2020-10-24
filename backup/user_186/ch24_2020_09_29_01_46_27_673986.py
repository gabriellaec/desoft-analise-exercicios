def calcula_aumento (salario):
    aumento=salario*taxa
    taxa=1
    if salario>1250:
        taxa=1/10
        return ("jjj", aumento)
    else:
        taxa=15/100
        return ("kkk", aumento)
    