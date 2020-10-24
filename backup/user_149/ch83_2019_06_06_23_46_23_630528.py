def medias_por_inicial(dicionario):
    
    nota = {}
    nome = []
    notas = []
    i = 1
    
    for k,v in dicionario.items():     
        nota[k[0]]=v
        nome.append(k[0])
        notas.append(v)
        
        
        
    for e in range(len(notas)):
        if nome[e-1]==nome[e]:
            m = notas[e-1]+notas[e]
            media = m/2
            #print(media)
            nota[nome[e-1]]=media
    
    return nota