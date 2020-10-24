def estritamente_crescente(numeros):
    i=0
while(i<len(numeros)):
        if (numeros[i+1]>numeros[i]):
            i+=1
    return (numeros)
