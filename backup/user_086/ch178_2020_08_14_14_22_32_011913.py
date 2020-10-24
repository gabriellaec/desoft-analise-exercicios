def junta_nomes(nomes1,nomes2,sobrenomes):
    x=0
    y=0
    z=0

    lista_nomes = []

    if len(nomes1)!=0:
        while x < len(nomes1):
            while z< len(sobrenomes):
                lista_nomes.append(nomes1[x]+" "+sobrenomes[z])
                z+=1
            z=0
            x+=1

    z=0

    if len(nomes2)!=0:
        while y < len(nomes2):
            while z< len(sobrenomes):
                lista_nomes.append(nomes2[y]+" "+sobrenomes[z])
                z+=1
            z=0
            y+=1 
    
    return lista_nomes