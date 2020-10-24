def junta_nome_sobrenome(nomes, sobre):
    nome_sobre = []
    e = ' '
    i = 0
    for y in nomes:
        nome_sobre.append(y + e + sobre[i])
        i += 1
    return nome_sobre