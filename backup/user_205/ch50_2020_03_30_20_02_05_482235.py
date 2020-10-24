def junta_nome_sobrenome(lista1,lista2):
    junto=[]
    for nome in lista1:
    	for sobrenome in lista2:
         	junto.append(["%s %s"] % (nome,sobrenome))
    return junto
      
        
   
    
        