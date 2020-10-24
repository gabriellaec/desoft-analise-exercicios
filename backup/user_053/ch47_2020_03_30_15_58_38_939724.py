def estritamente_crescente(lista):
    nova_lista = [lista[0]]
    i = 0
    maior_elemento = nova_lista[0]
    
    while i < len(lista):
        if lista[i] > maior_elemento:
            maior_elemento = lista[i]
            nova_lista.append(lista[i])
        i += 1
    return nova_lista

a = [10, 15, 11, 12, 13, 14]
b = estritamente_crescente(a)            
print(b)