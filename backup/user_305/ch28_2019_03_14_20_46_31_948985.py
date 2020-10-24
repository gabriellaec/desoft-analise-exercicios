a = int(input('Qual a velocidade do seu hotwheels?'))
if a>80:
    print ('voce foi pego na malandragem')
    multa = ((a-80) * 5)
    print ('{0:.2f}'.format(multa)
else:
    print ('Não foi multado')
    
        
        