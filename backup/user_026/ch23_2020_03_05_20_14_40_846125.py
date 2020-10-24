veloc= int(input( "diga a velocidade do carro (em km/h): "))
if veloc> 80 :
    print("voce foi multado")
    valor= (80-veloc)*5
    print("sua multa foi de {0}".format(valor))
else:
    print("Não foi multado")