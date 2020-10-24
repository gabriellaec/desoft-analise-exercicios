distancia=int(input('Qual distância você deseja percorrer(em km)? '))
if distancia <=200:
    preco=0.5*distancia
    print('Sua passagem será {0:2f}.'.format(preco))
else:
    preco=0.45*distancia
    print('Sua passagem será {0:2f}.'.format(preco))