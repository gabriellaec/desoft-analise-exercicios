def verifica_preco(t_livro,dicionario,cor):
    titulos = list(dicionario.keys())
    cores = list(t_livro.values())
    nome_do_livro = list(cor.keys())
    valor = list(cor.values())
    for a in range(len(titulos)):
        if t_livro == titulos[a]:
            valor = cores[a]
            break
    cordolivro = cores[a]
    for a in range(len(valor)):
        if valor == nome_do_livro[a]:
            return valor[a]