def calcula_media(l):
    val=[]
    for i in range(len(l)):
        for nota in l[i].values():
            val.append(nota)
    return(sum(val)/len(val))