def apaga_repetidos (string):
    
    ja_usadas = []
    string = string.lower()
    
    for l in string:
        if l in ja_usadas: 
            string.replace(l, '*')
        elif l not in ja_usadas:
            ja_usadas.append(l)
            
            
    return string