def calcula_aumento(salario):
    aumento=1.15
    if salario>=1250:
        aumento=1.10
    salario_final=salario*aumento
    return float(salario_final)

        
       