def remove_vogais(lista):
    resp=[]
    for vogal in lista:
        if vogal !="a" or vogal !="e" or vogal != "i" or vogal != "o" or vogal != "u":
            resp.append(vogal)
            
  	return resp

remove_vogals(lista)