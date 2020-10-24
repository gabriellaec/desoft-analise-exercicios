def lista_primos(numero_indice):
    lista_primeiros_primos = []
    i = 0
    numero_primo = 1
    while i < numero_indice - 1:
        if numero_primo % 3 != 0 and numero_primo % 5 != 0 and numero_primo % 7 != 0:
            lista_primeiros_primos.append(numero_primo)
            numero_primo += 1
        else:
            numero_primo += 1
    return lista_primeiros_primos