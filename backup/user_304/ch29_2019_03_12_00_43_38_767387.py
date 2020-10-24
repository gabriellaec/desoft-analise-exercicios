def calcula_aumento (salário):
    if salário> 1250:
        aumento=salário*0.1
    else:
        aumento=salário*0.15
salario=int(input('qual é o seu salário? '))
print('seu aumento é de {0:.2f}'.format (aumento))
