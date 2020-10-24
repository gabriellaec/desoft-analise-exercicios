def eh_crescente(lista):
    i=0
    while i < len(lista):        
        if lista == sorted(lista,reverse=True):
            return False
            
        elif lista == sorted(lista):
            return True
            
        else:
            return False
        i+=1
            