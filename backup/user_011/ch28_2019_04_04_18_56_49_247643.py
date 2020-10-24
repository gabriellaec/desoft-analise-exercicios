velocidade=int(input('Qual sua vel? '))
if velocidade>=80:
    valor=(velocidade-80)*5
    print('Você foi multado, R$'valor)
else:
    print('Não foi multado')