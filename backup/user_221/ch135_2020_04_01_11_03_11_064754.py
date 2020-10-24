def equaliza_imagem(intensidade, k):
    nova_lista = []*len(intensidade)
    i = 0
    while i < len(lista):
        if intensidade[i]*k > 255:
            nova_lista.append(intensidade[i])
        if intensidade[i]*k < 255:
            intensidade[i] = intensidade[i]*k
            nova_lista.append(intensidade[i])
        i = i + 1
    return nova_lista
            
            