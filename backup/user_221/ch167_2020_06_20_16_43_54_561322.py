def bairro_mais_custoso(bairros):
    novo_dicionario = {}
    i = 6
    y = 0
    s = 0
    pop = ''
    for nome, lista in bairros.items():
        while i < len(lista):
            y += bairros[nome][i]
            i += 1
        i = 6
        novo_dicionario[nome] = y
        y = 0
    for nome, total in novo_dicionario.items():
        d = novo_dicionario[nome]
        if s < d:
            s = d
            pop = nome
    return nome