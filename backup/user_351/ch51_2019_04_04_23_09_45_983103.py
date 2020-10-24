def estritamente_crescente(numeros):
    i=1
    crescente=[]
    maior = numeros[0]
    crescente.append(numeros[0])
    while i< len(numeros):
        if numeros[i]>maior:
            crescente.append(numeros[i])
            maior = numeros[i]
        i+=1
    return crescente
        
        