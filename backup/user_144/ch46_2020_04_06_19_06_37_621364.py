def numero_no_indice(lista):
    new_list = []
    i = 0
    while i < len(lista):
        if lista[i] == i:
            i+=1
            new_list.append(i)
            
    return new_lista
        
        
    

      
#def numero_no_indice(lista):
  #  new_list = []
   # for i in range(len(lista)):
    #    if lista[i] == i:
     #       new_list.append(i)
    #return new_list