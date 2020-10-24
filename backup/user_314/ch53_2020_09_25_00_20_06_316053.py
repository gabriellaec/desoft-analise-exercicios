def impar (num):
  
    if(num%2==0):
        return False
    else:
        return True


def soma_impares (lista):

    j=0
    soma=0

    while(j<len(lista)):
        
        r=impar(lista[j])
        
        if r:
            soma+=lista[j]
        j+=1

    return soma
