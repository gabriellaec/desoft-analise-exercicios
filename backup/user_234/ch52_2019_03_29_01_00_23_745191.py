def eh_crescente(lista):
    i=1
    num_lista = len(lista)
    while i < num_lista:
        if lista[i] > lista[i+1]:
            return True
        else:
            return False