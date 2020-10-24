contagem= 0
def conta_ocorrencias(lista):
    contagem={}
    i=2
    for n in lista :
        if not n in contagem:
            contagem[n]=1
        else:           
            contagem[n] = i
        i += 1
        return contagem
        