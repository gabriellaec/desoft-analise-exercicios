
def conta_ocorrencias (palavras):
    dicio = {}
    for word in palavras:
        if word in dicio:
            dicio[word] += 1
        else:
            dicio[word] = 1

    return dicio

def mais_frequente (palavras):
    dicio = conta_ocorrencias(palavras)
    count = 0
    max = ''
    for k, v in dicio.items():
        if v > count:
            count = v
            max = k
    
        
    return max
