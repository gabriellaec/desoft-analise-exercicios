def calcula_fibonacci(n):
    fi =[0]*n
    fi[0] = 1
    fi[1] = 1
    for i in range(len(fi)):
        fi[i] = fi[i-1] + fi[i-2]
    return fi