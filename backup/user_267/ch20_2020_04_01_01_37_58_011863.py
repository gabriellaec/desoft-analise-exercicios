pergunta_distancia = int(input('Qual a distancia da sua viagem em km? '))
def funcao_preco():
    if pergunta_distancia <= 200:
        preco = 0.5*pergunta_distancia
    else:
        preco = 0.5*200 + 0.45*(pergunta_distancia - 200)
    return preco
       