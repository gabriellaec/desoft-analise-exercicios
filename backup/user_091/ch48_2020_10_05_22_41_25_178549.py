def eh_crescente(lista):
    max=lista[0]
    i=1
    while i<len(lista)-1:
        if lista[i]>max:
            max=lista[i]
            i+=1
            if  max==lista[len(lista)-1]:
                return True
            else:
                return False
        else:
            i+=1
            

    