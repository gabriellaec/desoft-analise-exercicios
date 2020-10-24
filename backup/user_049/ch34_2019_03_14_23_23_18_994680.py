deposito=input('Qual é o valor do depósito?')
juros=input('Qual é a taxa de juros?')

contador=1

while contador<24:
    contador+=1
    y=deposito*juros/100
    print (y)