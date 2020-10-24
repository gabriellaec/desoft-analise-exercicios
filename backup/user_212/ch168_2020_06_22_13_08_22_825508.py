def login_disponivel (nome, login_uso):
    
    if nome not in login_uso:
        return nome 
    else:
        i = 0
        while True: 
            i += 1
            string = nome + str(i)
            if string not in login_uso:
                return string 
          
            
    
    
            
        