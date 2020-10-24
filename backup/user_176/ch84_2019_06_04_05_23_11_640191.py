def inverte_dicionario(entrada):
    saida = {}
    for k, v in entrada.iteritems():
        saida[v] = saida.get(v, [])
        saida[v].append(k)