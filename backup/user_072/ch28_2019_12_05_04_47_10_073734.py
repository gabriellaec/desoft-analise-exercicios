a=int(input('Qual a velocidade do carro? '))

if a<=80:
    print ('Não foi multado')
else:
    print ('Voce foi multado em R$ {0:.2f}'.format((a-80)*5))

