def junta_listas(lista):
    lista2 = []
    i = 0
    while i < len(lista):
        e = 0
        while e < len(lista[i]):
            if lista[i][e] not in lista2:
                lista2.append(lista[i][e])
                e+=1
        i +=1
    return lista2

    
# Usando FOR    
#def junta_listas(lista):
 #   lista2 = []      
  #  for i in range(len(lista)):
   #     for e in range(len(lista[i])):
    #        if lista[i][e] not in lista2:
     #           lista2.append(lista[i][e])
            
