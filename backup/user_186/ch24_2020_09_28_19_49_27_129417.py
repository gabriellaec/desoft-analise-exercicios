def calcula_aumento (salario):
    aumento = salario*taxa
    taxa=1
    if salario>1250:
        taxa=1/10
    elif salario<=1250:
        taxa=15/100
    else :
        print ("Deu errado")
    