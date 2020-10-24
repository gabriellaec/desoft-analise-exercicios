lista = []
a = str(input("Digite uma palavra: "))
while a != "fim":
    if a[0] == "a":
        lista.append(a)
        a = str(input("Digite uma palavra: "))
    else:
        a = str(input("Digite uma palavra: "))
        
print(lista)
