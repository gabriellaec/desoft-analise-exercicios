def verifica_preco(titulo, dic_titulos, dic_precos):
    if titulo in dic_titulos:
        cor = dic_titulos[titulo]
        if cor in dic_precos:
            preco = dic_precos[cor]
    return preco