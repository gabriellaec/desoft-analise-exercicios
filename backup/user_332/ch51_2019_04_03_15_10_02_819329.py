def estritamente_crescente (lista):
    final = []
    for e in lista:
    	maior = lista[0]
    	final.append(maior)
        if(e > maior):
            maior = e
            final.append(e)
    return final
