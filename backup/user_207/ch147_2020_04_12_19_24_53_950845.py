lista_palavras = []

def mais_frequente (lista_palavras):
    def conta_ocorrencias (lista_palavras):
    dicio = {}
    for word in lista_palavras:
        if word in dicio:
            dicio[word] +=1
        else:
            dicio[word] =1
    return dicio
    max = 0
    palavra_mais_frequente = '0'
    for v in dicio.values():
        if max < v:
            max = v
    for k, v in dicio.items():
        if v == max:
            palavra_mais_frequente = k
    return palavra_mais_frequente
