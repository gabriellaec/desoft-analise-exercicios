def conta_a(palavra):
    lista=list(palavra)
    cont=0
    i=0
    while(i<len(lista)):
        if(lista[i]=="a"):
            cont+=1
    return cont
   