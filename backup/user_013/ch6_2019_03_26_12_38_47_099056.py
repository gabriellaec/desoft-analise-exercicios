def encontra_maximo(M):
    # Contador
    n = 0
    # Lista de Ganhadores G:
    G = []*3
    # Looping
    while n <= 2:
        if M[n][0] > M[n][1] and M[n][0] > M[n][2]:
            G[n] = M[n][0]
        elif M[n][1] > M[n][0] and M[n][1] > M[n][2]:
            G[n] = M[n][1]
        else:
            G[n] = M[n][2]
        n += 1
    if G[0] > G[1] and G[0] > G[2]:
        return G[0]
    elif G[1] > G[0] and G[1] > G[2]:
        return G[1]
    else:
        return G[2]