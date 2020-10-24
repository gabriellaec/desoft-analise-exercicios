def conta_ocorrencias(lista_1):
    dicionario={}
    lista=[]
    contador=[]
    for i in lista_1:
        if i not in lista:
            lista.append(i)
        else:
            contador+=1
