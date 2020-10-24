def total_do_semestre_por_bairro(bairros):
    novo_dicionario = {}
    i = 6
    y = 0
    for nome, lista in bairros.items():
        while i < len(lista):
            y += bairros[nome][i]
            i += 1
        i = 6
        novo_dicionario[nome] = y
        y = 0
    return novo_dicionario

def bairro_mais_custoso(bairros):
    novo_dicionario = total_do_semestre_por_bairro(bairros)
    s = 0
    pop = ''
    for nome, valor in novo_dicionario.items():
        m = novo_dicionario[nome]
        if m > s:
            s = m
            pop = nome
    return pop