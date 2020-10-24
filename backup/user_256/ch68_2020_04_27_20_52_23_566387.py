def separa_trios(lista_nomes):
    i = 0 
    total=[]
    while i < len(lista_nomes):
        trio =[]
        while len(trio) < 3 and i < len(lista_nomes):
            trio.append(lista_nomes[i])
            i+=1
        total.append(trio)
        
    return total