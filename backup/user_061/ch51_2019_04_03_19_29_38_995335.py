def estritamente_crescente(lista):
    maior = lista[0]
    contador = 0
    crescente = []
    while contador < len(lista):
        if maior <= lista[contador]:
            crescente.append(lista[contador])
            maior = lista[contador]
            contador += 1
        else:
            del lista[contador]
    f = 0
    sem_rep = []
    while f<len(crescente):
        if crescente[f] not in sem_rep:
            sem_rep.append(crescente[f])
        f+=1
    return sem_rep
