contagem= 0
def conta_ocorrencias(lista):
    contagem={}
    i=0
    for n in lista :
        if not n in contagem:
            contagem[n] = i
        i += 1
        return contagem
        