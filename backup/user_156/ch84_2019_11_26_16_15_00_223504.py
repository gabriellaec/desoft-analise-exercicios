def inverte_dicionario(dicionario):
    inv_dicionario = {}
    for k, v in dicionario():
        inv_dicionario[v] = inv_dicionario.get(v, [])
        inv_dicionario[v].append(k)
    		return inv_dicionario
    