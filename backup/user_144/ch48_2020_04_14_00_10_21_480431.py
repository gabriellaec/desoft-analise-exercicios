def eh_crescente(lista):
    i=0
    while i < len(lista):        
        if len(lista) < 2: 
            return False
            
        elif lista[i] == lista[i+1]:
            return False
            
        elif lista == sorted(lista,reverse=True):
            return False
            
        elif lista == sorted(lista):
            return True
            
        else:
            return False
        i+=1
            