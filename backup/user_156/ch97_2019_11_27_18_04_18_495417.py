def total_do_semestre_por_bairro(dicionario):
    saida = {}
    
    for k, v in dicionario.items():
        for k in dicionario.keys():
            saida[k].append(k)
        for v in dicionario.values():
            i = 5
            soma = 0
            while i <= 12 and i >= i:
                soma += v[i]
                i += 1
            saida[v].append(soma)
    return saida
