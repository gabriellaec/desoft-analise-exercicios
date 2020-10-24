with open("texto.txt","r") as arquivo:
    lista=arquivo.spit()
    contador=lista.count()
print(contador)