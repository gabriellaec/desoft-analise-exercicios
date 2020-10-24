def lista_primos(numero_indice):
    lista_primeiros_primos = []
    i = 0
    numero_primo = 0
    while i < numero_indice:
        if numero_primo < 3:
            numero_primo += 1    
            lista_primeiros_primos.append(numero_primo)
            i += 1
        else:
            if numero_primo % 3 != 0 and numero_primo % 5 != 0 and numero_primo % 7 != 0:
                lista_primeiros_primos.append(numero_primo)
                numero_primo += 3
                i += 1
            elif numero_primo == 5 or  numero_primo == 7:
                lista_primeiros_primos.append(numero_primo)
                numero_primo += 2
                i += 1
            else:
                numero_primo += 2
    print(len(lista_primeiros_primos))
    print(lista_primeiros_primos)
    return lista_primeiros_primos