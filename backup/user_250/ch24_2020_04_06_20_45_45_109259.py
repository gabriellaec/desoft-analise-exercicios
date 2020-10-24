def calcula_aumento(salario):
    if salario > 1250:
        novosalario = 1.1*salario
        aumento = novosalario-salario
        return aumento
    else:
        novosalario = 1.15*salario
        aumento = novosalario-salario
        return aumento