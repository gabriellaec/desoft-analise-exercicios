def inverte_dicionario(entrada):
    saida={}
    for nome,idade in entrada.items():
        lista=[]
        if idade not in saida:
            lista.append(nome)
            saida[idade]=lista
        else:
            lista.append(nome)
    return saida