def mais_populoso(dicio_estadosbr):
    new_estados = []
    new_num = []
    maior = 0
    for estado,dicio_resto in dicio_estadosbr.items():
        new_estados.append(estado)
        total = 0
        for cidade,pop in dicio_resto.items():
            total += pop
            new_num.append(pop)
    i = 1
    for n in new_num:
        if n[i] > n[i-1]:
            maior = n[i]
        n += 1
    return (new_estados[i])
            
        
            
        
        