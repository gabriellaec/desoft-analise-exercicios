def bairro_mais_custoso(saida):
    mais_caro = []
    key_maior = []
    
    for i in saida.keys():
        key_maior.append(i)
        mais_caro.append(len(saida[i]))
    
    maiscaro = max(mais_caro)
    
    return key_maior[mais_caro.index(maiscaro)]

