pergunta_distancia = int(input('Qual a distancia da sua viagem em km? '))
x = pergunta_distancia

def funcao_preco(x):
    if x <= 200:
        preco = 0.5*x
    else:
        preco = 0.5*200 + 0.45*(x - 200)
    return preco
       