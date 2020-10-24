def medias_por_inicial(notas):
    
    medias = {}
    alunos_por_inicial = {}
    
    for nome in notas.keys():
        
        inicial = nome[0]
        
        if inicial not in medias.keys():
            medias[inicial] = notas[nome]
            alunos_por_inicial[inicial] = 1
        
        else:
            medias[inicial] += notas[nome]
            alunos_por_inicial[inicial] += 1
        
    for inicial in medias.keys():
        
        medias[inicial] /= alunos_por_inicial[inicial]
    
    return medias