def inverte_dicionario(normal):
    invertido = dict()
    for nome, idade in normal.items():
        if idade not in invertido.keys():
            n = list()
            n.append(nome)
            invertido[idade] = n
        else:
            for idade_inv, n in invertido.items():
                if idade == idade_inv:
                    n.append(nome)
    return invertido

            
       