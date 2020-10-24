contagem= 0
def conta_ocorrencias(lista):
    contagem={}
    i=1
    for n in lista :
        contagem[n] = i
        i += 1
        return contagem
        