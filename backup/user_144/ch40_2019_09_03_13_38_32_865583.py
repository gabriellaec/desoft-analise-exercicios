def fatorial(n):
    if n == 1:
        return 1
    # se não retornou até agora é porque n > 1
    return fatorial(n - 1) * n