lista= []
x= int(input("Numero 1: ")
lista.append(x)
y= int(input("Numero 2: ")
lista.append(y)
z= int(input("Numero 3: ")
lista.append(z)
lista_nova= []

def numero_no_indice(lista):
    i = 0
    for e in lista:
        if e == i:
            lista_nova.append(e)

        i+=1 
    return lista_nova
print(numero_no_indice(lista))