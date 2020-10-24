def verifica_progressao(lista):
    if len(lista)> 1:
        r = lista[1] - lista[0]
        if lista[0] != 0:
            q = lista[1]/lista[0]
        pa = True
        pg = True
        i = 0
        k = 0
        for a in lista:
            if a == 0:
                pg = False
        while pa and i < len(lista) - 1:
            if lista[i+1] - lista[i] != r:
                i+=1
                pa = False
        while pg and k < len(lista) -1:
            if lista[i+1] / lista[i] != q:
                k +=1
                pg = False
        if pa and pg == True:
            return "AG"
        elif pa == True:
            return "PA"
        elif pg == True:
            return "PG"
        else:
            return "NA"
            
     