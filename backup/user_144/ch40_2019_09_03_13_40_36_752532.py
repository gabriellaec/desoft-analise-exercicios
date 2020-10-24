def fatorial(n):
    if n < 0:
        print('Não está definido.')
        return
    if n == 0 or n == 1:
        return 1
    return fatorial(n - 1) * n