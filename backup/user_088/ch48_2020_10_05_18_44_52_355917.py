def eh_crescente(lista):
    i=0
    cont=0
    while(i<len(lista)-1):
        if(lista[i]<lista[i+1]):
            cont=+1
        i+=1
    if(cont==len(lista)-1):
         return True
    else:    
         return False