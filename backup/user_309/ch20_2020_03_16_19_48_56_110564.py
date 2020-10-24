dist = int(input('Distancia que deseja percorrer em km: '))

if dist <= 200:
    preco_final = 0.50 * dist
else:
    preco_final = preco_final + (dist-200)*0.45
    


print('O preco da sua passagem é: {0:.2f}R$'.format(preco_final))