def eh_crescente(lista):
    crescente = True
    i = 1
    while i < len(lista):
        if lista[i] >= lista[i-1]: 
            crescente = True
        if lista[i] <= lista[i -1]:
            crescente = False
        i = i + 1
    if crescente:
        return True
    else: 
        return False

print(eh_crescente([1,2,3,5,4])