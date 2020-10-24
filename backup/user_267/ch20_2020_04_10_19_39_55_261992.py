def funcao_preco(x):
    if x <= 200:
        preco = 0.5*x
    else:
        preco = 100 + (0.45*(x - 200))
    return preco

pergunta_distancia = int(input('Qual a distancia da sua viagem em km? '))
a = pergunta_distancia
print(funcao_preco(a))
       