def separa_trios(lista):
    i=0
    trios=[]
    while i <= len(lista):

        trios.append(lista[i:i+3])

        i+=2
        
   
    return trios
