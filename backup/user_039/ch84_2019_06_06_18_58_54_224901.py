def inverte_dicionario(dict):
    dictnovo={}
    for k,v in dict.items():
        if v not in dictnovo:
            dictnovo[v]=[k]
        else:
            dictnovo[v].append(k)
    return dictnovo
    