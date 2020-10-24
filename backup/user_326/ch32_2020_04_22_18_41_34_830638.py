def lista_primos(numero_indice):
    lista_primeiros_primos = []
    i = 1
    numero_primo = 2
    while len(lista_primeiros_primos) < 100:
        eh_primo = True
        i = 2
        while i < len(lista_primeiros_primos):
            if numero_primo % lista_primeiros_primos[i] == 0:
                eh_primo = False
                break
            else: 
                i += 1
        if eh_primo:
            lista_primeiros_primos.append(numero_primo)
            numero_primo += 1
        else:
            numero_primo += 1
    print(lista_primeiros_primos)
    return lista_primeiros_primos