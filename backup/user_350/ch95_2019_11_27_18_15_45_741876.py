def mais_populoso(dic):
    maior = 0
    soma = 0 
    for k,v in dic.items():
        for municipio in v:
            soma += v[municipio]
            if soma > maior:
                maior = k
    return maior