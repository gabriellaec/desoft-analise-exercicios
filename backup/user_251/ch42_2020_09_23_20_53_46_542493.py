lista = []
a = str(input("Digite uma palavra: "))
indice = 0
while a != "fim":
    if a[0] == "a":
        lista.append(a)
        a = str(input("Digite uma palavra: "))
        indice += 1
    else:
        a = str(input("Digite uma palavra: "))
n = 0
while n < indice:
    print(lista[n])
    n += 1      

