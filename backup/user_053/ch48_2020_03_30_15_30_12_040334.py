def eh_crescente(lista):
    i = 0
    while i < (len(lista) - 1):
        if lista[i+1] <= lista[i]:
            resultado = False
            i = len(lista)
        else:
            i += 1
            resultado = True
    return resultado

a = [2, 3, 15, 7, 9, 10]
b = eh_crescente(a)

print(b)