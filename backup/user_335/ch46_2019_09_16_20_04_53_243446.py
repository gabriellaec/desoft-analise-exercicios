def PreencherLista ():
    lista = []
    p = input ("Digite uma palavra: ")
    lista.append(p)
    while p != "fim":
        p = input ("Digite uma palavra: ")
        lista.append(p)
    return lista

def InicioA(listaP):
    i = 0
    while i < len(listaP):
        if listaP[i][0] == "a":
            print (listaP[i])
            i += 1
        else:
            i += 1

l = PreencherLista()
InicioA(l)