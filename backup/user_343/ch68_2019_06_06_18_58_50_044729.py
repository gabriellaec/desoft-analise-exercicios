def separa_trios(lista):
    i=0
    trios=[]
    while i < len(lista):
        trio=[]
        trio.append(lista[i:i+2])
        trios.append(trio)
        i+=1
        
   	return trios