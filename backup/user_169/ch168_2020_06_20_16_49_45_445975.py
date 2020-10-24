def login_disponivel(string,lista):
    
    
   
    if string not in lista:
        return string   
    else:
        contador=0
        for i in lista:
            if i[:len(string)] == string:
                contador+=1
        return string + '{0}'.format(contador)
        
        