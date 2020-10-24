def monta_dicionario(chaves,valores):
    dic={}
    i=0
    while i<len(chaves):
        dic[chaves[i]]=valores[i]
        i+=1
    return dic