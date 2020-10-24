
def calcula_euler(x, n):
    c = 0
    d = 0
    e = 0
    euler = 0
    while c < n:
        euler += (x ** c)/d
        c += 1
        d *= e
        e += 1
    return euler

        