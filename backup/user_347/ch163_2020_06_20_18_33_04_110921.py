def calcula_media (lista):
    nova = []
    for i in lista:
        for o in i:
            nova.append(i[o])
    soma = 0
    for k in nova:
        soma += k
    return (soma/len(nova))