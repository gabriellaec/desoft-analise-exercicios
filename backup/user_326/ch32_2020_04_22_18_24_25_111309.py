def lista_primos(numero_indice):
    lista_primeiros_primos = []
    i = 0
    numero_primo = 1
    while len(lista_primeiros_primos) < 100:
        print(len(lista_primeiros_primos))
        eh_primo = True
        while i < len(lista_primeiros_primos) - 1:
            if numero_primo % lista_primeiros_primos[i] == 0:
                eh_primo = False
                print('hey2')
                break
            else: 
                i += 1
        if eh_primo:
            lista_primeiros_primos.append(numero_primo)
            numero_primo += 1
        else:
            numero_primo += 1
    return lista_primeiros_primos