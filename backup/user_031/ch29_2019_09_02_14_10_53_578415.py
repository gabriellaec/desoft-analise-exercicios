def calcula_aumento (salario):
    aumento = 0.15
    if salario > 1250:
        aumento = 0.10
    aumento_total = salario * aumento
    return(aumento_total)