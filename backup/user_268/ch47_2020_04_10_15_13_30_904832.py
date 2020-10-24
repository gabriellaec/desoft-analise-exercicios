def estritamente_crescente(lista):
    a = len(lista)
    listo = []
    z = 0
    if a == 0:
        return listo
    else:
        listo.append(lista[0])
        for i in range(1, a):
            if lista[i] > listo [z]:
                listo.append(lista[i])
                z+=1
            
        return listo
                
                