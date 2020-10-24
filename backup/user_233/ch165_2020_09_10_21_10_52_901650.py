
def mais_populoso(brasil):
    
    populacao_estados = dict()
    
    for estado in brasil.keys():
        populacao_estados[sum(brasil[estado].values())] = estado
    
    populacao_maxima = max(populacao_estados.keys())
    
    return populacao_estados[populacao_maxima]

