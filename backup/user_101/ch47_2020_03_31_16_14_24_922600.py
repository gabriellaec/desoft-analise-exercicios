def estritamente_crescente(l):
    if len(l) != 0:
        indice = 1
        listaFinal = []
        listaFinal.append(l[0])
        while indice < len(l):
            doidera = l[0:indice]
            indiceDoidera = 0
            while indiceDoidera < indice: 
                if l[indice] > doidera[indiceDoidera]:
                    listaFinal.append(l[indice])
                indiceDoidera += 1
            indice += 1
        return listaFinal
    else:
        return l
            