def verifica_progressao(lista):
    """Função que retorna se lista é uma PA ou uma PG."""

    pa = True #flag da PA
    pg = True #flag da PG

    if len(lista) < 2:
        return "NA"
    elif len(lista) == 2:
        return "AG"

    indice_pa = lista[1]-lista[0]
    indice_pg = lista[1]/lista[0]

    i = 1
    while i < len(lista)-1:
        if lista[i+1]-lista[i] != indice_pa:
            pa = False
            break
        i += 1

    i = 1
    while i < len(lista)-1:
        if lista[i+1]/lista[i] != indice_pg:
            pg = False
            break
        i += 1

    if pa and pg:
        return "AG"
    elif pa:
        return "PA"
    elif pg:
        return "PG"
    else:
        return "NA"
