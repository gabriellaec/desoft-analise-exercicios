
distancia = float(input('Insira a distância que deseja percorrer em km: '))

if distancia <= 200:
    preco = distancia * 0.50
    print ('O preço da passagem ficou: {0:.2f}'.format(preco))

else:
    preco = (distancia - 200) * 0.45 + (200 * 0.50)
    print ('O preço da passagem ficou: {0:.2f}'.format(preco))