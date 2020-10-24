def verifica_progressao(L):
    rA = L[1] - L[0]
    if L[0] == 0:
        rG = L[2] / L[1]
    else:
        rG = L[1] / L[0] 
    for n in range(1, len(L)):
        if L[n] == L[n - 1] + (1) * rA  and  L[n] == L[n - 1] * rG * 1:
            Resultado="AG"
        elif L[n] == L[n - 1] + (1) * rA:
            Resultado="PA"               
        elif L[n] == L[n - 1] * rG * 1 :
            Resultado="PG"
        else:
            return"NA"
    return Resultado