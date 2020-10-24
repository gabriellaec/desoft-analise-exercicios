def acha_bigramas(s):
    lista = []
    i = 0
    while i < len(lista)-1 :
        if not (s[i] + s[i+1]) in lista :
            lista.append(s[i]+s[i+1])
        i+=1
    return lista
    print lista