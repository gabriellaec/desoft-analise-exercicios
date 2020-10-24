def estritamente_crescente(lista):
    for i in lista:
        if i[i] > i[i-1]:
            lista.append(i)
        else:
            del (i)
            