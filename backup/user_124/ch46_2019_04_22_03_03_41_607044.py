palavra = input("digite uma palavra / 'fim' para terminar: ")
lista = []
lista.append(palavra)
def conta_letra_a(texto):
    contador = 0
    i = 0
    if palavra == "fim":
        print(lista)
    
    while i < len(texto):
        if texto[i] == 'a':
            contador += 1
        i += 1
    return contador