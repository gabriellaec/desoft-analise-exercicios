def estritamente_crescente(Lista_Numero):
    Lista_Nova_Cresc = []
    i = 0
    while i<=(len(Lista_Numero)):
        if Lista_Numero[i]<Lista_Numero[i+1]:
            Lista_Nova_Cresc.append(Lista_Numero)
        else:
            print("Lista não crescente")
        i+=1
    return Lista_Nova_Cresc