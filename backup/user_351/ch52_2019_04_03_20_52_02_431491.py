def eh_crescente(lista):
    i=0
    maior = lista[i]
    while lista[i]>lista[i+1]:
        i+=1
        return True
    else:
        return False 
    
