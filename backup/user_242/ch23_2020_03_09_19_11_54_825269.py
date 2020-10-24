VELOCIDADE = int(input ('Digite a velocidade em km/h'))
if VELOCIDADE > 80:
    print ('Foi multado')
    valor = (VELOCIDADE -80) * 5
    print('sua multa foi de {0:.2f}'.format(valor))    
else:
    print('Não foi multado')    
