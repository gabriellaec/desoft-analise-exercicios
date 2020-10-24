def funcao_preco(x):
    if x <= 200:
        preco1 = 0.5*x
        return preco1
    else:
        preco2 = 100 + (0.45*(x - 200))
        return preco2

pergunta_distancia = int(input('Qual a distancia da sua viagem em km? '))
a = pergunta_distancia
print(funcao_preco(a))
       