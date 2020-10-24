def medias_por_inicial(notas):
    media = dict() # dicionario de retorno
    conta_iniciais = dict() # dicionario que conta ocorrencias
    soma_notas = dict() # dicionario que conta notaas
    for nome, nota in notas.items():
        if nome[0] not in conta_iniciais:
            conta_iniciais[nome[0]] = 1
            soma_notas[nome[0]] = nota
        else:
            conta_iniciais[nome[0]] += 1
            soma_notas[nome[0]] += nota
    for inicial in conta_iniciais:
        media[inicial] = soma_notas[inicial] / conta_iniciais[inicial]
    return media
    
            
        
            
        
    