def bairro_mais_custoso(dicionario):
    semestre={}
    for c in dicionario:
        for i in range(6,12):
            if c not in semestre:
                semestre[c]=dicionario[c][i]
            else:
                semestre[c]+=dicionario[c][i]
    return semestre