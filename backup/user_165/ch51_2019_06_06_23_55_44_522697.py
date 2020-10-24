def estritamente_crescente(Lista_Numero):
    Lista_Nova_Cresc = []
    i = -1
    for i in range(len(Lista_Numero)-1):
        if Lista_Numero[i]<Lista_Numero[i+1]:
            Lista_Nova_Cresc.append(Lista_Numero[i+1])
    return Lista_Nova_Cresc