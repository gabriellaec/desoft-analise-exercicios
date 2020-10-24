def calcula_euler(x ,n):
    exx = 1 + x
    for i in range (n):
        exn = (exx + x**n / 2*n)
        return exn

    