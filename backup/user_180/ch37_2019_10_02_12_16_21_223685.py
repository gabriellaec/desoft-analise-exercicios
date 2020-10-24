def lista_primos(n):
    lista_primeiros = []
    contador = 1
    check_primo = "nao"
    if contador == 0 or contador == 1:
        check_primo = "nao"
    elif contador == 2:
        check_primo = "sim"
    elif contador % 2 == 0:
        check_primo = "nao"
    else:
        x = 3
        while x < contador:
            if contador % x == 0:
                check_primo = "nao"
            x = x + 2
        if x == contador:
            check_primo = "sim"
        else:
            check_primo = "nao"
    while contador > len(lista_primeiros):
        if check_primo == "sim":
            lista_primeiros.append(contador)
        contador += 1
        else:
            continue
    return lista_primeiros