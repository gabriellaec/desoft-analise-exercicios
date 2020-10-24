lista = []
palavra = str(input("Por favor, digite uma palavra :"))
while palavra != "fim":
    lista.append(palavra)
    print(palavra)
    palavra = str(input("Por favor, digite uma palavra :"))
print(lista)