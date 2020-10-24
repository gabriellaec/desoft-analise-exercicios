def calcula_aumento(v):
    salario = v
    if v > 1250:
        salario = 0.1*v
    else:
        salario = 0.15*v
    return salario