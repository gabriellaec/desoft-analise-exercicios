def encontra_maximo(mat):
    a = mat[0][0]
    for i in mat:
        for j in mat[i]:
            if j > a:
                a = j
    return a
            
            