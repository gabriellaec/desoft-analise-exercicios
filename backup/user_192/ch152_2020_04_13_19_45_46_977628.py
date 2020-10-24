def verifica_preco(titulo, nome_cor, cores_preco):
    nome_cor = dict()
    cores_preco = dict()
    c = list()
    preco_final = list()
    for nome in nome_cor.keys():
        if nome == titulo:
            c.append(nome_cor[nome])
    for cor2 in cores_preco.keys():
        for i in range(len(c)):
            if c[i] == cor2:
                preco_final.append(cores_preco[cor2])
        return preco_final
            