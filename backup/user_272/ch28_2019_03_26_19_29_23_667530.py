velocidade=int(input('qual foi a velocidade?:')
valor=0
if velocidade>80:
    valor=(velocidade-80)*5
    print('voce recebeu uma multa de ',valor)
else:
    print('Não foi multado')