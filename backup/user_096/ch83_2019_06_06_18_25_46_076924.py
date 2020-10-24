dicionario = {'Andrew Ayres': 6, 'Fábio Ikeda': 10, 'Fábio Kurauchi': 9, 'Raul Hage': 8}
def medias_por_inicial(dicionario):
    soma = {} 
    iniciais = {}
    media = {}
    for k,v in dicionario.items():
        
        if k[0] in soma:
            soma[k[0]] += v
            iniciais[k[0]] += 1
        if k[0] not in soma: 
            soma[k[0]] = v
            iniciais[k[0]] = 1
    for q,w in iniciais.items():
        media[q] = soma[q]/w
            
    return media