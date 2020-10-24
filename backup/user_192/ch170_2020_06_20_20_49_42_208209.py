def apaga_repetidos(txt):
    for i in txt:
        if txt[i] in txt:
            a = txt.replace(txt[i], '*')
    return a
        
    
            