def eh_crescente(lista):
    i = 0
    while i+1<len(lista):
        if lista[i+1]<= lista[i]:
            i += 1
            return False
            
           
        else:
            return True
      