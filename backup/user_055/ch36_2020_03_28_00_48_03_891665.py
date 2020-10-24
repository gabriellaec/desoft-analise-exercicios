def fatorial(n):
    n_fatorial = [n]
    i = 1
    while len(n_fatorial) < n:
        n_fatorial.append(n - i)
        i += 1
    resultado = 1
    for x in n_fatorial:
        resultado = (resultado * x)
    return resultado