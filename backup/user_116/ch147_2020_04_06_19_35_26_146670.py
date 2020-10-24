def conta_ocorrencias(lista):
    i=0
    u=0
    contador=0
    
    dicionario={}
    while i<len(lista):
        if u<len(lista):
            if lista[i]==lista[u]:
                contador+=1
                u+=1

            else:
                u+=1
        else:
            
            dicionario[lista[i]]=contador
            contador=0
            u=0
            i+=1
    listx= dicionario       
    return listx
def mais_frequente(listx):
    lista2=[]
    diciva={}
    for n in listx.values():
        lista2.append(n)
    z=max(lista2)
    for p,q in listx.items():
        diciva[q]=p
    return diciva[z]

listx=conta_ocorrencias(lista)
lista2=mais_frequente(listx)
