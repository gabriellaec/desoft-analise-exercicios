def separa_trios (lista):
    grupos = []
    grupox = []
    i = 1
    for a in lista:
        if(i <= 3):
            grupox.append(a)
            i += 1
        else:
            grupos.append(grupox)
            i = 2
            grupox = []
            grupox.append(a)
    return(grupos)