def mais_frequente(x):
    d = {}
    i = 0
    maior = 0
    for e in x:           
        if e in d:
            d[e] += 1
        if e not in d:
            d[e] = 1 
    
    for u,t in d:
        if t > maior:
            maior = t
        else:
            maior = maior
    return maior
       
    





