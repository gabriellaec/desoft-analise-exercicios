def PiWalllis(elementos):
    i = 1
    lista = []
    while i <= elementos:
        lista.append((i+1)/i)
        i += 1 
    meio_pi = 1
    for numero in lista:
        meio_pi = meio_pi*numero
    pi = 2*meio_pi
    return pi