def conta_letras(string):
    dic = {}
    letras=[]
    valores=[]
    for i in range(len(string)):
        if string[i] not in letras:
            letras.append(string[i])
            valores.append(1)
        else:
            for e in range(len(letras)):
                if string[i]==letras[e]:
                    valores[e]+=1
    for j in range(len(letras)):
        dic[palavras[j]]=valores[j]
    return dic