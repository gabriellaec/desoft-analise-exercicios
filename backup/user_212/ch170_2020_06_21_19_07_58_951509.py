def apaga_repetidos (string):
    
    ja_usadas = []
    #string = string.lower()
    string = list(string)
    nova_string = []
    
    for l in string:
        
        if l in ja_usadas: 
            nova_string.append('*')
            
        elif l not in ja_usadas:
            nova_string.append(l)
            ja_usadas.append(l)
            
    nova_string = ''.join(nova_string)
            
    return nova_string