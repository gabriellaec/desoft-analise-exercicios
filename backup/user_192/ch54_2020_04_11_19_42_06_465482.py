def calcula_fibonacci(n):
    fi = []*n
    fi[0] = 1
    fi[1] = 1
    i=0
    while i < len(fi):
        f[i] = f[i-1] + fi[i-2]
        i+=1
    return fi