distancia = float(input('Qual a distancia que você deseja percorrer em km? '))
if distancia < 200:
    passagem = 0.5 * distancia
    return ('{0:.2f}'.format(passagem))
else:
    passagem = 0.45 * (distancia-200)
    return ('{0:.2f}'.format(passagem))

