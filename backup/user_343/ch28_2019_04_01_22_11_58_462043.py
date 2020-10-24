a=int(input('velocidade?'))
if a>80:
    c=(a-80)*5
    print('Foi multado, {:.2f}'.format(c))
else:
    print('Nao foi multado')