def verifica_preco(titulo, dicionario_nomeEcor, dicionario_corEpreco):
    tit_livro = str(titulo)
    for tit_livro in dicionario_nomeEcor.items():
        if tit_livro == titulo:
            cor = dicionario_nomeEcor[titulo]

    for cores, valores in dicionario_corEpreco.items():
        if cor == cores:
            valor = dicionario_nomeEcor[cores]
    return valor