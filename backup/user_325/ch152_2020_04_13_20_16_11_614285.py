def verifica_preco(nome,dictitulo,diccor):
    nomes=list(dictitulo.keys())
    valorcor=list(dictitulo.values())
    nomelivro=list(diccor.keys())
    valorlivro=list(diccor.values())
    for i in range(len(nomes)):
        if nome==nomes[i]:
            valornome=valorcor[i]
            break
    corlivro=valorcor[i]
    for i in range(len(valorlivro)):
        if valornome==nomelivro[i]:
            return valorlivro[i]