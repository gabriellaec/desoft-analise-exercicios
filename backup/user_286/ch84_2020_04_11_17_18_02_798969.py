def inverte_dicionario(dic):
    dic_invertido = {}
    for nome, idade in dic.items():
        if idade not in dic_invertido.keys():
            nome = [nome]
            dic_invertido[idade] = nome
        else:
            for idade_inv, nome_inv in dic_invertido.items():
                if idade == idade_inv:
                    nome_inv.append(nome)

    return dic_invertido