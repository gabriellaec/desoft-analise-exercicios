def verifica_preco(nome,dictitulo,diccores):
    titulo = list(dictitulo.keys())
    valorcor = list(dictitulo.values())
    nomelivro = list(diccores.keys())
    valorlivro = list(diccores.values())
    for i in range(len(titulos)):
        if nome==titulos[i]:
            valornome=valorcor[i]
            break
    corlivro=valorcor[i]
    for i in range(len(valorlivro)):
        if valornome==nomelivro[i]:
            return valorlivro[i]