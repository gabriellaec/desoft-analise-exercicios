def verifica_preco(t_livro,dictitulos,diccores):
    titulos = list(dictitulos.keys())
    cores = list(t_livro.values())
    nome_do_livro = list(diccores.keys())
    valor = list(diccores.values())
    for a in range(len(titulos)):
        if t_livro == titulos[a]:
            valor = cores[a]
            break
    cordolivro = cores[a]
    for a in range(len(valor)):
        if valor == nome_do_livro[a]:
            return valor[a]