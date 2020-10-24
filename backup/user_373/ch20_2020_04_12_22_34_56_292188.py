distancia= float(input('Qual distancia?: '))
if distancia <= 200.0:
    passagem= distancia*0.5
    print ('Preço: R$ {0:.2f}'.format(passagem))
else:
    passagem= (distancia- 200) *0.45 +100
    print ('Preço: R$ {0:.2f}'.format(passagem))
    
    