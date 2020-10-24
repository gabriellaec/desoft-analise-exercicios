def verifica_preco(titulo, nome_cor, cores_preco):
    nome_cor = dict()
    cores_preco = dict()
    for nome, cor1 in nome_cor.items():
        if nome == titulo:
            c = nome_cor[nome]
    for cor2, preco in cores_preco.items():
        if c == cor2:
            preco_final = cores_preco[cor2]
        return preco_final
            