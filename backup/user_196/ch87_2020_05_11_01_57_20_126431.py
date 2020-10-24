with open ("churras.txt", "r") as arquivo:
    lista = arquivo.readlines()
    for i, k in enumerate(lista):
        k += lista[i+1] * lista[i+2]
    print (k)    