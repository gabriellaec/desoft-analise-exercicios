def eh_crescente(lista):
    print(lista)
    if lista == [] or len(lista) == 1:
        return True
    for i in range(len(lista)-1):
        if lista[i+1] > lista[i]:
            return True
        else:
            return False
 
        