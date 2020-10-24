def conta_letras(a):
    dic={}
    for letra in a:
        if letra not in dic:
            dic[letra] = 1
        else:
            dic[letra]+=1

    return dic