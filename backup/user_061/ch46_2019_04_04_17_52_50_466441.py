palavra = input("Defina uma palavra")
lista = []
lista.append(palavra)

while palavra != "fim":
    palavra = input("Defina uma palavra")
    lista.append(palavra)

def palavra_inicia_a(lista):
    lista_a = []
    i = 0
    while i < len(lista):
        string = lista[i]
        if string[0] == "a":
            lista_a.append(string)
        i+=1
    return lista_a