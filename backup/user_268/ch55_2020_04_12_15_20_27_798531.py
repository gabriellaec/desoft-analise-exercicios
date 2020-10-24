def encontra_maximo(mat):
    a = 0
    for i in mat:
        for j in mat[i]:
            if j > a:
                a = j
            else:
                a = a
    return a
            