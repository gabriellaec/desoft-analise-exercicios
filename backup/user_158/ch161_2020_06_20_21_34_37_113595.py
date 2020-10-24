def PiWallis(n):
    numeradores =[2]
    denominadores =[1]
    lista_bask = [2/1]
    for n in range(1,n):
        if (n % 2) != 0:
            lista_bask.append(numeradores[-1]/(denominadores[-1]+2))
            denominadores.append(denominadores[-1]+2)
        if(n % 2) == 0:
            lista_bask.append((numeradores[-1]+2)/denominadores[-1])
            numeradores.append(numeradores[-1]+2)
    meio_pi = 1
    for t  in lista_bask:
        meio_pi = t*meio_pi
    pi = 2*meio_pi
    return pi