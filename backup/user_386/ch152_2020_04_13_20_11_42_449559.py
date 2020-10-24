def verifica_preco(nome,dicionario_livros,tab_cores):
    for x,y in dicionario_livros.items():
        if x == nome:
            for key,values in tab_cores.items():
                if key == y:
                    return values