def junta_nome_sobrenome(listanomes, listasobrenomes):
    nomeesobrenome = []
    i = 0
    while i < len(listanomes):
        nomecompleto = listanomes[i]+" "+listasobrenomes[i]
        nomeesobrenome.append(nomecompleto)
        i += 1
    return nomeesobrenome