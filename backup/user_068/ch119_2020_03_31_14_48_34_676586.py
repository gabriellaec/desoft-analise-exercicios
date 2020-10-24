
def calcula_euler(x, n):
    c = 0
    d = 1
    e = 1
    euler = 0
    while c < n:
        euler += (x ** c)/d
        c += 1
        d *= e
        e += 1
    return euler
