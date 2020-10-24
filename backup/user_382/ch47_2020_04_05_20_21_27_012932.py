def estritamente_crescente(l1):
    if l1 == []:
        return l1
    else:
        maximo = l1[0]
        lista = [maximo]
        i = 0 
        while i < (len(l1)-1):
            if l1[i+1] > maximo:
                maximo = l1[i+1]
                lista.append(l1[i+1])
            i += 1
        return lista