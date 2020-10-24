distancia = float(input('Digite a distância:'))
def preco_passagem(distancia):
    if distancia <= 200:
        preco = distancia*0.50
    elif distancia > 200:
        preco = 100 + (distancia-200)*0.45
    resposta = 'O preço da passagem é de R$: {}'.format(round(preco, 2))
    return resposta
print(preco_passagem(distancia))