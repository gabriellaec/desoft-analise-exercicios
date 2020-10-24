def estritamente_crescente(lista):
    if lista:
        str_cres = [lista[0]]
        i = 1
        while i < len(lista):
            curr_element = lista[i]
            if curr_element > str_cres[-1]:
                str_cres.append(curr_element)
            i += 1
    return str_cres
    