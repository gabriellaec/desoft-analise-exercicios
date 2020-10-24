def apaga_repetidos(txt):
    for i in range(len(txt)):
        if txt[i] in txt:
            txt.replace(txt[i], '*')
    return txt
        
            
      
    
            