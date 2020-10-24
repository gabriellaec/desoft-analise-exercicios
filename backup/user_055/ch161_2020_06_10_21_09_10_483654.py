def piWallis(x):
    lista_n = [2]
    lista_d = [1]
    lista_pi = [2/1]
    for x in range(1, x):
        if x % 2 != 0:
            lista_pi.append(lista_n[-1]/(lista_d[-1] + 2))
            lista_d.append(lista_d[-1] + 2)
        if x % 2 == 0:
            lista_pi.append((lista_n[-1] + 2)/lista_d[-1])
            lista_n.append(lista_n[-1] + 2)
    meio_pi = 1
    for t in lista_pi:
        meio_pi = t * meio_pi
    print(meio_pi*2)