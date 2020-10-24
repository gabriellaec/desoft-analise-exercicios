def eh_crescente(lista):
    i=0
   
    while(i<len(lista)):
        if(lista[i+1]<=lista[i]):
            return False
        elif(lista[i+1]>list[i]):    
            
            return True
        i+=1