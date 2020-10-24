def media_por_inicial(nome_nota):
    inicial = {}
    for nome,nota in nome_nota.items():
        if not nome[0] in inicial:
            inicial[nome[0]] = nota
            
        else:
            ocorrencia = 1
            s = inicial[nome[0]]
            ocorrencia += 1
            s = (s*(ocorrencia-1))+nome_nota[nome] 
            inicial[nome[0]] = s/ocorrencia
    return inicial