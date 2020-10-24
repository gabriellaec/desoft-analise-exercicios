def acha_bigramas(palavra):
    i=0
    lista=[]
    while i < len(palavra)-1:
        lista.append(palavra[i]+palavra[i+1])
        i+=1
    return lista
b='babador'
print(acha_bigramas(b))