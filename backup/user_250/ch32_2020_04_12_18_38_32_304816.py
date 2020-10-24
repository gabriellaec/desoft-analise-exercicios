def lista_primos(n):
    if n == 0:
        return []
    lista = [2]
    primo = 3
    while len(lista) < n:
        i = 1
        while i < primo:
            i = i+1
            if primo %i == 0:
                break
            if i == primo-1:
                lista.append(primo)
        primo = primo+1
    return lista
         
        

    