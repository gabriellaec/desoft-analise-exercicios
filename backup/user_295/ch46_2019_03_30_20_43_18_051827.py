palavra = input ("Fala uma palavra")

lista = []

while palavra != "fim":
    lista.append(palavra)
    palavra = input ("Fala uma palavra")
 


i = 0

while i < len(lista):
    if (lista[i])[0] != "a":
        i +=1
    
    else:
        print (lista[i])
        i += 1