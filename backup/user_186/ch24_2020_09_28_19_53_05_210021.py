def calcula_aumento (salario):
    taxa=1   
    aumento = salario*taxa
    if salario>1250:
        taxa=1/10
        return ("jjj", aumento)
    else:
        taxa=15/100
        return ("kkk", aumento)
    