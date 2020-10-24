def junta_listas(lista):
    listacomp = []
    for i in range (len(lista)):
        listacomp.append([map(''.join, lista)])
    return listacomp
        