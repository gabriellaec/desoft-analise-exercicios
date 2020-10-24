def login_disponivel (string, lista_uso):
    nome = string
    
    if nome not in lista_uso:
        return string 
    
    else: 
        i = 1
        while string in lista_uso:
            string = nome + str(i)
            i +=1
            
        return string
            
        