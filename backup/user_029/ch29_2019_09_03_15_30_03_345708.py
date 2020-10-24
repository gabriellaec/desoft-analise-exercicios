def calcula_aumento(x):
    
    salario = 0
    if x > 1250:
        salario = x + (x*0.1)
    else:
        salario = x + (x*0.15)
    return x