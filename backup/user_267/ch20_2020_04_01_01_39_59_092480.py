

def funcao_preco(x):
    if x <= 200:
        preco = 0.5*x
    else:
        preco = 0.5*200 + 0.45*(x - 200)
    return preco
       