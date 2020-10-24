def inverte_dicionario(d):
    novo_d = {}
    for nome,idade in d.items(): 
        if idade not in novo_d:
            novo_d[idade]= [nome]
        else:
            novo_d[idade].append(nome)
    return novo_d