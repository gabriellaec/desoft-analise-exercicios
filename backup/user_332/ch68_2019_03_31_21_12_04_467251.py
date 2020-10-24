def separa_trios (lista):
    grupos = []
    i = 1
    for a in lista:
        grupox = []
        if(i <= 3):
            grupox.append(a)
            i += 1
        else:
            grupos.append(grupox)
            i = 1
        grupox = []
    return(grupos)