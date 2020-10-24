with open("texto.txt","r") as arquivo:
    lista=arquivo.split()
    contador=len(lista)
print(contador)