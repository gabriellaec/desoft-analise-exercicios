def apaga_repetidos(txt):
    for i in range(len(txt)):
        if txt[i] in txt:
            txt[i] == '*'
    return txt
            
      
    
            