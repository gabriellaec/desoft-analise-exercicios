deposito=int(input('Qual é o valor do depósito? '))
juros=int(input('Qual é a taxa de juros? '))
contador=0
while contador<24:
    contador+=1
    taxa=(deposito*juros/100)
    y=contador*taxa+deposito
    print ("Valor da mês é: R$ {0:.2f}".format(y))
valor_ganho=(deposito*juros/100)*24
print ("Valor total ganho é: R$ {0:.2f}".format(valor_ganho))