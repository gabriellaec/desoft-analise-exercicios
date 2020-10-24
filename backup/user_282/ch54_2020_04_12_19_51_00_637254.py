def calcula_fibonacci(n):
    fi = [1, 1]
    lista = []
    for i in range(n):
        a = fi[i+1] + fi[i]
        fi.append(a)
        lista.append(fi[i])
    return lista