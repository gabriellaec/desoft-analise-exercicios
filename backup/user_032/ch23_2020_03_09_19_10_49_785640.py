velocidade= int(input('Qual é a velocidade(em Km/h'))
if velocidade > 80:
    print('Você foi multado')
    valor= (velocidade-80)*5
    print("Sua multa foi de {0:.2f}".format(valor))
else: 
    print('Não foi multado')