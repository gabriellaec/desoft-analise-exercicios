a=int(input('qual é a velocidade do seu carro? '))
if a>80:
    v=(a-80)*5
print('sua multa foi de {0}'.format(v))
else:
print ('você não foi multado')
