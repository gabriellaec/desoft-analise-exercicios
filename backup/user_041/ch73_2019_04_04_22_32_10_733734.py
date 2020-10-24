def remove_vogais(palavra):
    lista=[]
    i=0
    while i<len(palavra):
        if palavra[i]!='a' or palavra[i]!='e' or palavra[i]!='i' or palavra[i]!='o' or palavra[i]!='u':
            lista.append(palavra[i])
      	i+=1
 	return lista       
        
 