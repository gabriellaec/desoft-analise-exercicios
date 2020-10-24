def separa_trios(entrada):
    saida = []
    i=0
    while i < len(entrada):
        entrada[i].append(saida)
        entrada[i+1].append(saida)
        entrada[i+2].append(saida)
        
        i+=1
    return saida