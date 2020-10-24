def mais_populoso(dicio_estadosbr):
    new_estados = []
    new_num = []
    maior = 0
    total = 0
    for estado,dicio_resto in dicio_estadosbr.items():
        new_estados.append(estado)
        for cidade,pop in dicio_resto.items():
            total += pop
        new_num.append(total)
        total = 0
    for i in range(len(new_num)):
        if new_num[i] > new_num[i-1]:
            maior = new_num[i]
    return (new_estados[i])
            
        
            
        
        