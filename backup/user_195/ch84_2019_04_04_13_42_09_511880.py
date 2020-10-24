def inverte_dicionario(D):
    C={}
    for nomes,anos in D.items():
        if anos in C:
            C[anos].append(nomes)
        else:
            C[anos]=[nomes]
    return C