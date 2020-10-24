n = int(input('Lista de números primos: '))
def lista_primos(n):
    if n == 0:
        return []
    lista = [2]
    n_primo = 3
    while len(lista) < n:
        for x in range(2,n_primo):
            if primo % x == 0:
                break
            if x == (primo - 1):
                lista.append(n_primo)
        n_primo += 1
    return lista