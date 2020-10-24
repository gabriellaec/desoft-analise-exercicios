dist=int(input('Qual distância, em km, deseja percorrer? '))

if dist<=200:
    preco=dist*0.50
    print('Preço da passagem, em reais: {0.:2f}'.format(preco))
else:
    preco=100+(dist-200)*0.45
    print('Preço da passagem, em reais: {0.:2f}'.format(preco))