def verifica_preco(titulo,dic_c,dic_nome):
    if titulo in dic_nome:
        cores = dic_nome[titulo]
        if cores in dic_c:
            preco = dic_c[cores]
            return preco