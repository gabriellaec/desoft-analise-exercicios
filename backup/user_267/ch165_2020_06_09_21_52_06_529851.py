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
    while i < len(new_num):
        if new_num[i] > new_num[i-1]:
            maior = new_num[i]
        i += 1
    return (new_estados[i])
            
        
            
        
        