def calcula_media (lista):
    nova = []
    for i in lista:
        for o in i:
            if i[o] not in nova:
                nova.append(i[o])
            else:
                nova.append(i[o])
    soma = 0
    for w in nova:
        soma += w

    return soma/len(nova)