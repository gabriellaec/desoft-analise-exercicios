palavra = input("Defina uma palavra ")
lista = []
lista.append(palavra)

f = 0
while palavra != "fim":
    palavra = input("Defina uma palavra ")
    lista.append(palavra)
    f+=1
    
del lista[f]

def palavra_inicia_a(lista):
    i = 0
    while i < len(lista):
        string = lista[i]
        if string[0] == "a":
            print(string)
        i+=1


palavra_inicia_a(lista)
            