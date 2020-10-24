def calcula_aumento(salario):
    if salario <= 1250:
        aumento = (salario * 15/100)
        return aumento
    else:
        aumento = (salario * 10/100)
        return aumento
        
       