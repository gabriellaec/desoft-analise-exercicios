def calcula_fibonacci(n):
    fi = [1, 1]
    for i in range(0, n-2):
        a = fi[i+1] + fi[i]
        fi.append(a)
    return fi