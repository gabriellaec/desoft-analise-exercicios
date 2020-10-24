def PiWallis(elementos):
    i = 1
    lista = []
    if elementos == 1:
        lista.append((i+1)/i)
    if elementos > 1:
        while i <= elementos:
            lista.append((i+1)/i)
            lista.append((i+1)/(i+2))
            i += 2 
    meio_pi = 1
    for numero in lista:
        meio_pi = meio_pi*numero
    pi = 2*meio_pi
    return pi