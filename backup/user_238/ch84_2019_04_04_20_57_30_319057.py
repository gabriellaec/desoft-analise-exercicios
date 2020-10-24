def inverte_dicionario(d):
    di={}
    for nomes, idades in d.items():
        if idades not in di:
            lista=[]
            lista.append(nomes)
            di[idades]=lista
        elif idades in di:
            lista=di[idades]
            lista.append(nomes)
            di[idades]=lista
    return di
d={'Ana': 19, 'Bruno': 18, 'João': 19}
print(inverte_dicionario(d))