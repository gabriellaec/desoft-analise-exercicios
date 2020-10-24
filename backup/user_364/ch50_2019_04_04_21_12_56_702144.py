lista= []
x= int(input("Fala ai"))
lista.append(x)
y= int(input("Fala ai 2"))
lista.append(y)
lista_nova= []

def numero_no_indice(lista):
    i = 0
    for e in lista:
        if e == i:
            lista_nova.append(e)

        i+=1 
    return lista_nova
print(numero_no_indice(lista))