def conta_ocorrencias(x):
    K = {}
    for palavra in x:
        if palavra in K:
            K[palavra]+= 1
        else:
            K[palavra]=1
    return K