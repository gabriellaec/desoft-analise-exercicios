def verifica_preco(livros,dic_nome_dos_livros,dic_cores):
    if livros in dic_nome_dos_livros:
        cores=dic_nome_dos_livros[livros]
    if cores in dic_cores:
        return dic_cores[cores]