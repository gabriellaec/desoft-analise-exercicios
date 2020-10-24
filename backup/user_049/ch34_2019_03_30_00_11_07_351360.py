deposito=int(input('Qual é o valor do depósito? '))
juros=int(input('Qual é a taxa de juros? '))
contador=0
while contador<24:
    contador+=1
    taxa=(deposito*juros/100)
    y=contador*taxa+deposito
    print (y)
valor_ganho=(deposito*juros/100)*24
print(valor_ganho)