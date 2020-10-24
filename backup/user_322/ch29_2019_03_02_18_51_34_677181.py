def aumento_salario(salario):
    if salario > 1250:
        aumento = salario + (0.1 * salario)
        return aumento
    else:
        aumento = salario * (1.15)
        return aumento
    
print(aumento_salario(500))