def zera_negativos(listainteiros):
    i=0
    while i<len(listainteiros):
        if listainteiros[i]<0:
            listainteiros[i]==0
        i+=1
    return listainteiros