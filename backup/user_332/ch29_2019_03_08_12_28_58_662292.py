def calcula_aumento(salario_atual):
    if(salario_atual > 1250):
        a = salario_atual * 0.1
        return(a)
    else:
        a = salario_atual * 0.15
        return(a)