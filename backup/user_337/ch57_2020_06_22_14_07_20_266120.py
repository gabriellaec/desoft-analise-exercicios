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
        while pa and i<len(lista)-1
            if lista[i+1] - lista[i] != r:
                pa = False
            i+=1
        while pg and k < len(lista)-1
            if lista[k+1] / lista[k] != q:
                pg = False
            k +=1
           
        if pa and pg == True:
            return "AG"
        elif pa == True:
            return "PA"
        elif pg == True:
            return "PG"
        else:
            return "NA"
            
     