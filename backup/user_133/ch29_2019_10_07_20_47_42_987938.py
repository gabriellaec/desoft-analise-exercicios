def calcula_aumento(salarioatual):
    if float(salarioatual) > 1250:
        aumento = 0.1 * float(salarioatual)
        return aumento
    else:
        aumento = 0.15 * float(salarioatual)
        return aumento
    