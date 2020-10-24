def estritamente_crescente(lista):
    int(lista)=[]
    i=0
    while i<int(len(lista)-1):
        if int(lista[i+1]>=lista[i]):
            int(lista.append(lista[i]))
        i=i+1
    return (lista)