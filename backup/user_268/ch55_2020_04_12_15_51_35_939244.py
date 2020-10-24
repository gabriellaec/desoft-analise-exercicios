def encontra_maximo(mat):
    a = mat[0][0]
    for i in mat:
        for j in i:
            if abs(j) >= a:
                a = abs(j)
            else:
                a = a
    return a
            
            