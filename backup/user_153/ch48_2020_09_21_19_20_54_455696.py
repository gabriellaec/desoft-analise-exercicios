def eh_crescente(lista):
    i = 0
    while i < len(lista) - 1:
        if lista[i+1] - lista[i] <= 0:
            return False
        i += 1
    return True

# lista = [1,2,4,4]
# print(eh_crescente(lista))