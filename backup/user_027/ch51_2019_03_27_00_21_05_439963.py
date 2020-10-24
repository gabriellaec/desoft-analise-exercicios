def maior_lista(x):
    i = 0
    maior = x[0]
    while i < len(x):
        if x[i] > maior:
            maior = x[i]
        i += 1
    return maior

def estritamente_crescente(x):
    lista = [x[0]]
    maior = x[0]
    for i in range(1,len(x)):
        if x[i] > maior_lista(lista):
            lista.append(x[i])
    return lista