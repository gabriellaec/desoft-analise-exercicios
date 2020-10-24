def verifica_preco(titulo, nome_cor, cores_preco):
    for nome, cor in nome_cor.items():
        if titulo in nome_cor:
            c = nome_cor[nome]
    for cor, preco in cores_preco.items():
        if c in cores_preco:
            c2 = cores_preco[cor]
    return c2
            