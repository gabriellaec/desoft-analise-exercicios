def estritamente_crescente(lista):
    i=0
    j=1
    resultado=[]
    if(len(lista)>0):
        resultado=[lista[0]]
    while(j<len(lista):
       if(lista[j]>resultado[i]):
           resultado.append(lista[j])
           i+=1
           j+=1
        else:
           j+=1
    return resultado
