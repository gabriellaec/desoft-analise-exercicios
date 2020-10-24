def separa_trios(x):
    i = 0
    lista = []
    while i < len(x):        
         
        lista.append(x[i:i+3])
        i += 3                   
    return lista
