def mais_frequente(x):
    d = {}
    maior = 0
    for e in x:           
        if e in d:
            d[e] += 1
        if e not in d:
            d[e] = 1 
    lista = list(d.keys())
    lista2 = list(d.values())
    
    return lista[lista2.index(max(lista2))]
       
    





