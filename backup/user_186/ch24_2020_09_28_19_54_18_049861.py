def calcula_aumento (salario):
    taxa=1   
    aumento = salario*taxa
    if salario>1250:
        aumento = salario*1/10
        return ("jjj", aumento)
    else:
        aumento = salario*1/15
        return ("kkk", aumento)
    