
def medias_por_inicial(notas):
    inicias = [nome[0] for nome in notas.keys()]
    notas_por_inicial = {}  
    for k, v in notas.items():
        notas_por_inicial[v] = notas.get(v, [])
        notas_por_inicial[v].append(k)
    
    return {inicial: sum(nostas)/len(notas) for nome,notas in notas_por_inicial.items()}