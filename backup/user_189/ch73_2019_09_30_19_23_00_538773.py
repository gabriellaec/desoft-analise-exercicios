def remove_vogais(lista):

    resp=[]
    lista=lista.split()
    for k in lista:
        for vogal in k:
            if vogal !="a" and vogal !="e" and vogal != "i" and vogal != "o" and vogal != "u":
                resp.append(vogal)
    
    if len(resp)==0:
        return None
        
    return resp

lista = "aeiou"
print(remove_vogais(lista))