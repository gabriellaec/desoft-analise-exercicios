def verifica_preco(nome, dic_nomescor, dic_corpreco):
    for n in dic_nomescor:
        if nome in dic_nomescor:
            cor = dic_nomescor[nome]
    for c in dic_corpreco:
        if cor in dic_corpreco:
            preco=dic_corpreco[cor]
    return preco