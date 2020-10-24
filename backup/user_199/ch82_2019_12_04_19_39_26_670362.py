palavra='meu pau de oculos'

def primeiras_ocorrencias(palavra):
    dic={}
    i=0
    while i<len(palavra):
        key=palavra[i]
        if key not in dic:
            dic[key]=0
        dic[key]+=1
        i+=1
    return dic
print(primeiras_ocorrencias(palavra))