def PiWallis(n):
    lista_n = [2]
    lista_d = [1]
    lista_pi = [2/1]
    for x in range(0, n):
        if x % 2 != 0:
            lista_pi.append(lista_n[-1] / (lista_d[-1] + 2))
            lista_d.append(lista_d[-1] + 2)
        if x % 2 == 0:
            lista_pi.append((lista_n[-1] + 2) / lista_d[-1])
            lista_n.append(lista_n[-1] + 2)
    meioPi = 1
    for t in lista_pi:
        meioPi = t * meioPi
    return meioPi * 2
