def verifica_pa(lista):
    i = 1
    while i < (len(lista) - 1):
        if lista[i] - lista [i-1] != lista[i+1] - lista[i]:
            return False
    return True
def verifica_pg(lista):
    f = 1
    while f < (len(lista) - 1):
        if lista[f] - lista [f-1] != lista[f+1] - lista[f]:
            return False
    return True
def verifica_progressao(lista):
    if verifica_pa(lista) == True and verifica_pg(lista) == True:
        return "AG"
    elif verifica_pa(lista) == True and verifica_pg(lista) == False:
        return "PA"
    elif verifica_pa(lista) == False and verifica_pg(lista) == True:
        return "PG"
    elif verifica_pa(lista) == False and verifica_pg(lista) == False:
        return "NA"