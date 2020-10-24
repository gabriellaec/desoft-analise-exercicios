def calcula_norma(A):
    #Lista de números maiores por linha
    M = [0]*3
    #Linha i (lembre-se: no Python, as coisas começam com zero)
    i = 0
    #Looping
    while i <=2:
        #Coluna j
        j = 0
        M[i] = abs(A[i][j])
        while j < 2:
            if abs(M[i]) < abs(A[i][j+1]):
                M[i] = abs(A[i][j+1])
            j += 1
        i += 1
    # Ganhador G
    G = M[0]
    if G < M[1]:
        G = M[1]
    if G < M[2]:
        G = M[2]
    return G