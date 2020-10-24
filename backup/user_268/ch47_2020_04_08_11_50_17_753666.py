def estritamente_crescente(lista):
    a = len(lista)
    res = [0]*a
    c = 0
        for i in range(a):
            for j in range(1, a):
                if lista[i] < = lista[j]:
                    res[c] = i
                    c+=1
    return res
                    