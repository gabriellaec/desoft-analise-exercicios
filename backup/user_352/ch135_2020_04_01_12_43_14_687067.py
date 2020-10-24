def equaliza_imagem(lista, k):
    x=lista*k
    resultado=[x]
    for x in resultado:
        if x>255:
            x=255
    return resultado
            
        
    
    
   