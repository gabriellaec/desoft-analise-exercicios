lista = []
x = input("ecreva uma palvra ")
if x[0] == "a":
    lista.append(x)
i = 0

while x != "fim":
    x = input("ecreva outra palvra ")
    if x[0] == "a":
        lista.append(x)
    
print (lista)
    


