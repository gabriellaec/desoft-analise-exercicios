def junta_listas(matriz):
    juntos = []
    n = len(matriz)
    i = 0
    while i < n:
        lista = matriz[i]
        l = len(lista)
        x = 0
        while x < l:
            juntos.append(lista[x])
            x += 1
        i += 1
    return juntos