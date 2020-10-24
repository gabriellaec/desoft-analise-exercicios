def estritamente_crescente (lista):
    crescente = []
    i = 0
    c = 0
    crescente.append(lista[i])
    while i+1<len(lista):
        if lista[i+1]>crescente[c]:
            crescente.append(lista[i+1])
            c+=1
        i+=1
    return crescente

#funcionou no vscode