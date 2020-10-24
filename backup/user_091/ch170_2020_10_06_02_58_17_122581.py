def apaga_repetidos(palavra):
    for e,x in palavra:
        if e==x:
            x='*'
        return palavra
        
         