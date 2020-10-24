with open ("churras.txt", "r") as arquivo:
    lista = arquivo.readlines()
    for i, k in enumerate(lista):
        k += lista[i] * lista[i+1]
    print (k)    