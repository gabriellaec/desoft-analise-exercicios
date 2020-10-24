def verifica_preco(nome,dicionario_livros,tab_cores):
    for a,b in dicionario_livros.items():
        if a == nome:
            for key,values in tab_cores.items():
                if key == b:
                    return values