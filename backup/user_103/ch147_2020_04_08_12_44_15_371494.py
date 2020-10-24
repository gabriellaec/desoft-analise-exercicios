def conta_ocorrencias(lista):
    dicionario={}
    i=0
    for i in lista:
        if not i in dicionario:
            dicionario[i]=1
        else:
            dicionario[i]+=1
 
    return dicionario

def mais_frequente(lista2):
    for lista2 in conta_ocorrencias:
        return max(dicionario)
        
    