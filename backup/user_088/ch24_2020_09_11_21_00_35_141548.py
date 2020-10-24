def calcula_aumento(salario):
    if (salario> 1250) :
        aumento=0.1*salario
        novo_salario=aumento+salario
        return novo_salario
    if(salario<=1250) :
        aumento=0,15*salario
        novo_salario=aumento +salario
        return novo_salario
        