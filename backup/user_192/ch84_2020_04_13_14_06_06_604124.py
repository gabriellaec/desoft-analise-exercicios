def inverte_dicionario(normal):
    invertido = dict()
    n = list()
    for nome, idade in normal.items():
        if idade not in invertido.keys():
            n.append(nome)
            invertido[idade] = n
        else:
            for idade_inv, n in invertido.items():
                if idade_inv == idade:
                    n.append(nome)
    return invertido

            
       