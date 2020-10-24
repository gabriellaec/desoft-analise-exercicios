def encontra_maximo(matrix):
    m = matrix[0][0]
    for linha in matrix:
        for elem in linha:
            if abs(elem) > abs(m):
                m = elem
    return m

matrix = [[-1, -2, -3], [-4, -15, -6], [-7, -8, -9]]
print(encontra_maximo(matrix))