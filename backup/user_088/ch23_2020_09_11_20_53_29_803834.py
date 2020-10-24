velocidade=(float(input('Diga a velocidade do carro'))
if (velocidade > 80):
       multa =(velocidade-80)*5
       print ('voce foi multa em R${0:.2f}'.format(multa))
if( velocidade<=80):
           print ('Não foi multado')