def lista_caracteres(string):
    lista_de_caracteres = []
    for i in string:
        if i in string:
            if i in lista_de_caracteres:
                continue
                
            else:
                lista_de_caracteres.append(i)
            
        
    return lista_de_caracteres
            
            