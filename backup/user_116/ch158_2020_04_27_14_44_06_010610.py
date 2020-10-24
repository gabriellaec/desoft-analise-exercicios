with open("texto.txt","r") as arquivo:
    lista=arquivo.split()
    contador=lista.count
print(contador)