def eh_crescente(lista):
    flag = 0
    i = 1
    while i < len(lista): 
        if(lista[i] < lista[i - 1]): 
            flag = 1
        i += 1
      
 
    if (not flag) : 
        return True 
    else :
        return False
     