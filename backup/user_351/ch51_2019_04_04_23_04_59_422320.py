def estritamente_crescente(numeros):
    i=1
    crescente=[]
    crescente.append(numeros[0])
    while i< len(numeros):
        if numeros[i]>numeros[i-1]:
            crescente.append(numeros[i])
        i+=1
    return crescente
        
        