dic1={'arroz': 1, 'batata': 3, 'coisa': 2}
dic2={'asas': 1,'oiue': 2, 'batata': 3}

def interseccao_chaves(dic1, dic2):
    lista=[]
    
    for k in dic1.keys():

    	for e in dic2.keys():
   			if k==e:
                
                lista.append(k)
                
    return lista
  
                       
                       