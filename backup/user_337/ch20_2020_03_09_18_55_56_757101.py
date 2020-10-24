distancia = float(input('Qual a distancia que você deseja percorrer em km?'))
if distancia < 200:
    preco = 0.50 * distancia
else:
    preco = 0.45 * distancia