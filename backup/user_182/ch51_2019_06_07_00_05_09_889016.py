def estritamente_crescente(Lista_Numero):
    Lista_Nova_Cresc = []
    i = 0
    while i<(len(Lista_Numero)):
        if Lista_Numero[i]>Lista_Numero[i+1]:
            break
        else:
            Lista_Nova_Cresc.append(Lista_Numero[i])
        i+=1
    return Lista_Nova_Cresc