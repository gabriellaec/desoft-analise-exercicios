def medias_por_inicial(notas):
    nomes = {}
    for k, v in notas.items():
        nomes[k[0]] = v
        print(nomes)
        for m, n in notas.items():
            if k[0] == m[0]:
                nomes[k[0]] += (n-v)/2
    return nomes