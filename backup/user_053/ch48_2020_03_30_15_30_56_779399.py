def eh_crescente(lista):
    i = 0
    resultado = True
    while i < (len(lista) - 1):
        if lista[i+1] <= lista[i]:
            resultado = False
            i = len(lista)
        else:
            i += 1
            
    return resultado

a = [2, 3, 15, 7, 9, 10]
b = eh_crescente(a)

print(b)