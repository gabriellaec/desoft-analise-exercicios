def mais_frequente(x):
    d = {}
    maior = 0
    for e in x:           
        if e in d:
            d[e] += 1
        if e not in d:
            d[e] = 1 
    
    for t in d:
        if t > maior:
            maior = t
        if t <= maior:
            maior = maior
    return maior
       
    





