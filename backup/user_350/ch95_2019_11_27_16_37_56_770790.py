def mais_populoso(dic):
    maior = dic[0]
    for k,v in dic.items():
        if v > maior:
            maior = v
    return maior