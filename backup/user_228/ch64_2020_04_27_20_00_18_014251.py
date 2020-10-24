def acha_bigramas(texto):
    lista=[]
    for i in texto:
        lista.append(texto[i]+texto[i+1])
    