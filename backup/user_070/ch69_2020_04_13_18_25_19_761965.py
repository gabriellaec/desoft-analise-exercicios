def junta_listas(matriz):
    juntos = []
    n = len(matriz)
    i = 0
    while i < n:
        juntos += matriz[i]
        i += 1
    return juntos