def verifica_preco(titulo,dicionario,cor):
    titulos = list(dicionario.keys())
    cores = list(titulo.values())
    nome_do_livro = list(cor.keys())
    valor = list(cor.values())
    for a in range(len(titulos)):
        if titulo == titulos[a]:
            valor = cores[a]
            break
    cordolivro = cores[a]
    for a in range(len(valor)):
        if valor == nome_do_livro[a]:
            return valor[a]