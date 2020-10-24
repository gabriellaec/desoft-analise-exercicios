def lista_sufixos(s):
    lista = []
    i = 0
    while i < len(s):
        a = s[i::1]
        lista.append(a)
        i+=1
        print(lista)
    return lista
   