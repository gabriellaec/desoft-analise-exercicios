def conta_ocorrencias(lista):
    dicionario=dict()
    for e in lista:
        if not e in dicionario:
            dicionario[e]=1
        else:
            dicionario[e]+=1
    return dicionario
def mais_frequente(lista):
    var=conta_ocorrencias(lista)
    maior = 0
    palavra=''
    for i in var:
        if var[i]>maior:
            palavra=i
            maior=var[i]
    return palavra
            
        