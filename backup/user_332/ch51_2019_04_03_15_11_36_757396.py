def estritamente_crescente (lista):
    final = []
    maior = lista[0]
    final.append(lista[0])
    for e in lista:
        if(e > maior):
            maior = e
            final.append(e)
    return final
