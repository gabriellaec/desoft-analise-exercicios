def verifica_preco(titulo,dicionario1,dicionario2):
    for i in dicionario1.keys():
        if i == titulo:
            for u in dicionario2.keys():
                if u == dicionario1[i]:
                    return dicionario2[u]