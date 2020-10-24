def equaliza_imagem(intensidades, k):
    
    equalizada = []
    
    for intensidade in intensidades:
        intensidade *= k
        if intensidade > 255: intensidade = 255
        equalizada.append(intensidade)
        