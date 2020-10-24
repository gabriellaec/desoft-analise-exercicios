def encontra_maximo(matriz):
    maiores = []
    for linha in matriz:
        max_linha = linha[0]
        for elementos in linha:
            if elementos > max_linha:
                max_linha = elementos
        maiores.append(max_linha)
    maximo = max(maiores)
    return maiores