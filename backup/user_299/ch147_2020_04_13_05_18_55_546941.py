
def conta_ocorrencias(lista):
    ocorrencias = {}
    for c in lista:
        if c in ocorrencias:
            ocorrencias[c] = ocorrencias[c] + 1
        else:
            ocorrencias[c] = 1
    return ocorrencias 

def mais_frequente(lista):
    ocorrencias = conta_ocorrencias(lista)
    nmax = 0
    palf = 'palavramaisfrequente'
    for stri, num in ocorrencias.items():
        if num > nmax:
            nmax = num
            palf = stri
    return palf