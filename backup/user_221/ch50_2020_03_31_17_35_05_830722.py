def junta_nome_sobrenome(n, s):
    n_s = []
    espaco = [' ']*len(n)
    i = 0
    while i < len(n):
        n_s.append(n[i] + espaco[i] + s[i])
        i = i + 1
    return n_s