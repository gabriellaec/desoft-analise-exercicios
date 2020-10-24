def calcula_aumento(salario):
    if salario <= 1250:
        novo = salario + (salario * 15/100)
    else:
        novo = salario + (salario * 10/100)
    return novo
        
       