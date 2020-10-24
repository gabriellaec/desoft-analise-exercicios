def eh_crescente(lista):
    if lista==[] or len(lista)==1:
        return True 
    else:
        for i in range (len(lista)-1):
            if lista[i+1]<=lista[i]:
                return False
            return True