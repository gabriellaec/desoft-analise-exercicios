def medias_por_inicial(a):
    dicionario = {}
    for nomes, valo in a.items():
        dicionario.setdefault(nomes[0], []).append(valo)
    for no, va in dicionario.items():
        va = sum(va)/len(va)
        dicionario[no] = va
    return dicionario
  