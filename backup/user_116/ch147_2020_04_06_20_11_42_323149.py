
def mais_frequente(lista):
    i=0
    u=0
    contador=0
    lista2=[]
    dicionario={}
    diciva={}
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
    for n in dicionario.values():
        lista2.append(n)
    for p,q in dicionario.items():
        diciva[q]=p

    z=max(lista2)
    return diciva[z]
