def calcula_aumento(salario):
    a = float(salario)
    if a > 1250:
        print(salario * 1.1)
    else:
        print (salario * 1.15)