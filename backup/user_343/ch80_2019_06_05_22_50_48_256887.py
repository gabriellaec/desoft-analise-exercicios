def interseccao_chaves(dic1, dic2):
    lista=[]
    
    for k in dic1.keys():

    	for e in dic2.keys():
   		
            if e==k:
               lista.append(k)

                   
                
    return lista