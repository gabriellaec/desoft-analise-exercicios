def separa_trios (lista):
    i=0
    nv=[]
    while i < len (lista):
        nv.append(lista[i:i+3])
        i+=3
        
        