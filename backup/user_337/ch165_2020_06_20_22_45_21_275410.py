def mais_populoso(dic):
    soma = 0
    lista = []
    for i in dic.values():
        for a in i.values():
            lista.append(a)
        for b in lista:
            s += b 
        if s>soma:
            soma = s
            break
    return soma