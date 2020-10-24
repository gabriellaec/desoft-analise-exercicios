def remove_vogais(lista):

    resp=[]

    for vogal in lista:
        if vogal !="a" and vogal !="e" and vogal != "i" and vogal != "o" and vogal != "u":
            resp.append(vogal)
        #print(vogal)
    return resp

lista = ["a","b","c","e",'f',"i"]
print(remove_vogais(lista))