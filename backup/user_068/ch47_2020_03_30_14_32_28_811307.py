def estritamente_crescente(a):
    lista = [1, 5, 6, 3,9]
    a = lista[0]
    i=0
    b = [a]
    while a < lista[i + 1]:
        b.append(lista[i+1])
        
    return True