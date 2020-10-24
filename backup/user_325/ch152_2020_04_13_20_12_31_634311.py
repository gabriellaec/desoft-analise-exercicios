def verifica_preco(nome,dicnome,diccor):
    nomes=list(dicnome.keys())
    valorcor=list(dicnome.values())
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