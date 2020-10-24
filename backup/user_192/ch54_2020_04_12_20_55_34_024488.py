def calcula_fibonacci(n):
    fi=[0]*n
    i=0
    fi[0] = 1
    fi[1] = 1
    while i <= n:
        fi[i] = fi[i-1] + fi[i-2]
        i+=1
    return fi