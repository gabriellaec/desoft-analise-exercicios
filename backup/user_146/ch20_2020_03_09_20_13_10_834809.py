def preco_passagem(km):
    if km <=200:
        preco = km*(0.5)
        return preco
    elif km >200:
        preco = 100 + (km - 200)*0.45
        return preco
a = int(input('Qual distancia deseja percorrer? '))
print('O preço da passagem é R$:{0:.2f}'.format(preco_passagem(a)))
