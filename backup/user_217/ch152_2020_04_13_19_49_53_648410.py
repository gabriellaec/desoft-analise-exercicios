def verifica_preco(nome,dic_livros,tab_cores):
    for k,v in dic_livros.items():
        if k == nome:
            for key,values in tab_cores.items():
                if key == v:
                    return values
     