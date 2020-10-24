def PiWallis(n):
    numeradores =[2]
    denominadores =[1]
    lista_bask = [(numeradores[0]/denominadores[0])]
    for i in range(1,n):
        if (i % 2) != 0:
            lista_bask.append(numeradores[-1]/denominadores[-1])
            denominadores.append(denominadores[-1]+2)
        else:
            lista_bask.append(numeradores[-1]/denominadores[-1])
            numeradores.append(numeradores[-1]+2)
    meio_pi = 1
    for t  in lista_bask:
        meio_pi = t*meio_pi
    pi = 2*meio_pi
    return pi