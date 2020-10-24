def inverte_dicionario(d):
    di={}
    for nomes, idades in d.items():
		if idades not in di:
            lista=[]
            di[idades]=lista.append(nomes)
        else:
            di[idades]=lista.append(nomes)
    return di
d={'Ana': 19, 'Bruno': 18, 'João': 19}
print(inverte_dicionario(d))
            