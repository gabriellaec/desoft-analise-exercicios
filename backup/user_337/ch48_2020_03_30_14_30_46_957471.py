def eh_crescente(lista):
    i = 0
    cresce = [lista[0]]
    while i<len(lista):
        if lista[i+1] <= lista[i]:
            return False
        	break
        else:
            cresce.append(lista[i+1])
            i += 1
    if len(cresce) == len(lista):
        return True
      
            
        