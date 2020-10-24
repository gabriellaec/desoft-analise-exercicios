def junta_nome_sobrenome(lista1,lista2):
    junto=[]
    for i in lista1:
    	for i in lista2:
         	junto.append(["%s %s"] % (lista1[i],lista2[i]))
    return junto
      
        
   
    
        