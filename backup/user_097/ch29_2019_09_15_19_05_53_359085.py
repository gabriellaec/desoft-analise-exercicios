def aumentoSalario(salario):
    if (salario>1250):
        aumento = (salario * 1.1) - salario
        return aumento
    elif (salario<=1250):
        aumento = (salario * 1.15) - salario
        return aumento

print("{0:.2f}".format(aumentoSalario(1251)))

