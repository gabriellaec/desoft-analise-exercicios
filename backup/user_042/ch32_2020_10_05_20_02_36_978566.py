lista = []

def lista_primos(n):
    len(lista) = n
    i = 0
    while i < len(lista):
        primo_lista = lista.append[i]
        i += 1
        a = 0
        if primo_lista[a] == 0:
            return False
        elif primo_lista[a] == 1:
            return False
        if primo_lista[a] == 2:
            return primo_lista[a]
        elif primo_lista[a] % 2 ==0:
            return False
        impares = 3
        while impares < primo_lista[a]:
            if primo_lista[a] % impares == 0:
                return False
            impares += 2
        a += 1
        return primo_lista