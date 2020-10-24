def encontra_maximo(mat):
    a = (mat[0][0]) ** 2
    for i in mat:
        for j in i:
            if (j ** 2) > a:
                a = j
            else:
                a = a
    return (a ** 1/2)
            
            