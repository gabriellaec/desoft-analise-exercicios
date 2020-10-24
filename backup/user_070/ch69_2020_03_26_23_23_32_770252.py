def junta_listas(matriz):
    juntos = []
    n = len(matriz)
    i = 0
    while i < n:
        lista = matriz[i]
        juntos += lista
        i += 1
    return juntos