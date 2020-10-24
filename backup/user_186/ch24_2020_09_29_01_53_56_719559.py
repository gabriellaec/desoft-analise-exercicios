def calcula_aumento(salario):
    taxa=1
    aumento=salario*taxa
    if salario>1250:
        aumento=salario*1/10
        print ("aumento de ", aumento)
    else :
        aumento=salario*15/100
        print ("aumento de  ", aumento)