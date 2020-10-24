soma = 0
maior = 0
strs = 0
def mais_populoso(dic):
    for i in dic:
        dicionariomunicipio = dic[i]
        for e in dicionariomunicipio:
            soma+= dicionariomunicipio[e]
            if soma>maior:
                maior = soma
                strs = i
    return i