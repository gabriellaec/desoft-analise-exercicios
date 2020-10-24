def estritamente_crescente(numeros):
    i=0
    if(len(lista)>0):
        resultado=[lista[0]]
    else:
        resultado=[]
    while(i+1<len(numeros)):
        if (numeros[i+1]>resultado[i]):
            resultado.append(lista[i+1])
        i+=1
    return (numeros)
