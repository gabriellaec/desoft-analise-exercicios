def eh_crescente(lista):
    i = 0
    while i < len(lista):
        if i == 0:
            i += 1
        
        elif lista[i] <= lista[0]:
            return False
        
        else:
            condicao = True
            a = 1
            while i-a != 0 and condicao:
                if lista[i] > lista[i-a]:
                    a += 1            
                
                else:
                    return False
          
            else:
                i += 1
    else: 
        return True