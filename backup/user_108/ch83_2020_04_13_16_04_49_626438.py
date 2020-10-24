
def medias_por_inicial(notas):
    notas_por_inicial = {}  
    for k, v in notas.items():
        notas_por_inicial[k[0] = notas_por_inicial.get(k[0], [])
        notas_por_inicial[k[0].append(v)
    
    return { inicial: sum(notas)/len(notas) for inicial,notas in notas_por_inicial.items()}