def junta_nome_sobrenome(n, s):
    n_s = []
    espaço = [' ']
    i=0
    while i < len(n)+1:
        n_s.append(n[i] + espaço[i] + s[i])
        i += 1
    return n_s