def classifica_lista (lista):
    c=0
    u=0
    if len(lista) < 2:
        return 'nenhum'
    else:
        for i in lista:
            if lista[i+1] > lista[i]:
                c+=1
            if lista[i+1]<lista[i]:
                u+=1
        if c == len(lista):
            return 'crescente'
        if u == len(lista):
            return 'decrescente'
        else:
            return 'nenhuma'
 
               
                
                
          
        