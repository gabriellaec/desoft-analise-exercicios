velocidade=(float(input('Diga a velocidade em km/h'))
if (velocidade >80):
            multa =(velocidade-80)*5
            print ('voce foi multa em R${0:.2f}'.format(multa))
else:
            print ('Não foi multado')