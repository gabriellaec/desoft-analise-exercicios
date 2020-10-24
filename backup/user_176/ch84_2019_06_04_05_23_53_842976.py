def inverte_dicionario(entrada):
    saida = {}
    for k, v in entrada.items:
        saida[v] = saida.get(v, [])
        saida[v].append(k)