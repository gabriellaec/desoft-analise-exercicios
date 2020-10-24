def primeiras_ocorrencias(palavra):
    novo_d = {}
    for i in palavra:
        if i not in novo_d:
            novo_d[i] = 1
        else:
            novo_d[i]+=1
    return novo_d