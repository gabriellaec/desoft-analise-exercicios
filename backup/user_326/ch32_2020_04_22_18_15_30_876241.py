def lista_primos(numero_indice):
    lista_primeiros_primos = []
    i = 0
    numero_primo = 0
    while len(lista_primeiros_primos) < 100:
        eh_primo = True
        if len(lista_primeiros_primos) > 1:
            while i < len(lista_primeiros_primos) - 1:
                if numero_primo % lista_primeiros_primos[i] == 0:
                    eh_primo = False
                    break
                else: 
                    i += 1
        elif eh_primo:
            lista_primeiros_primos.append(numero_primo)
            numero_primo += 1
        else:
            numero_primo += 1
    return lista_primeiros_primos