def verifica_progressao(lista):
    if len(lista)> 1:
        r = lista[1] - lista[0]
        if lista[0] != 0:
            q = lista[1]/lista[0]
        pa = True
        pg = True
        for a in lista:
            if a == 0:
                pg = False
        while pa:
            for i in range(len(lista)-1):
                if lista[i+1] - lista[i] != r:
                    pa = False
        while pg:
            for i in range(len(lista)-1):
                if lista[i+1] / lista[i] != Q:
                    pg = False
        if pa and pg == True:
            return "AG"
        elif pa == True:
            return "PA"
        elif pg == True:
            return "PG"
        else:
            return "NA"
            
     