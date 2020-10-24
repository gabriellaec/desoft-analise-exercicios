def zera_negativos(lista_n):
    i = 0
    nova_lista = []
    while i < len(lista_n):
        num = lista_n[i]
        if num < 0:
            num = 0
            nova_lista.append(num)
        elif num >= 0:
            nova_lista.append(num)
        i += 1 
        
    return nova_lista