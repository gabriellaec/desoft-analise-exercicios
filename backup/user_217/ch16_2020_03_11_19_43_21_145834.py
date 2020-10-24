pergunta = float(input('Distancia percorrida: '))

if pergunta <= 200:
    valor=pergunta*0.5
    print('Preço= ','{:02.2f}'.format(valor))
else:
    valor=100+pergunta*0.45
    print('Preço= ','{:02.2f}'.format(valor))