def apaga_repetidos(txt):
    nova_string = ''
    for i in range(len(txt)):
        if txt[i] not in nova_string:
            nova_string += txt[i]
        else:
            nova_string += '*'
    return nova_string
        
            
      
    
            