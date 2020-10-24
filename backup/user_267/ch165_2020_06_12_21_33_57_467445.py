def mais_populoso(dicio_estadosbr):
    new_estados = []
    new_num = []
    maior = 0
    for estado,dicio_resto in dicio_estadosbr.items():
        total = 0
        new_estados.append(estado)
        for cidade,pop in dicio_resto.items():
            total += pop
        new_num.append(total)
    for i in range(len(new_num)):
        if new_num[i] > maior:
            maior = new_num[i]
            indice = i
    return (new_estados[indice])
            
        
            
        
        