def estritamente_crescente(numeros):
    i=0
    while(i<len(numeros)-1):
        if (numeros[i+1]<numeros[i]):
            numeros.remove(numeros[i])
        i+=1
    return (numeros)
