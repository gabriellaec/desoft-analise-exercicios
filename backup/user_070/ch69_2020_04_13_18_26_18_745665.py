def junta_listas(matriz):
    juntos = [0]*len(matriz)
    n = len(matriz)
    i = 0
    while i < n:
        juntos [i] += matriz[i]
        i += 1
    return juntos